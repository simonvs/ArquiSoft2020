import pika
import time
import os
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="mydatabase"
)

mycursor = mydb.cursor()


########### CONNEXIÓN A RABBIT MQ #######################
HOST = os.environ['RABBITMQ_HOST']

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST))
channel = connection.channel()

#El consumidor utiliza el exchange 'nestor'
channel.exchange_declare(exchange='nestor', exchange_type='topic', durable=True)

#Se crea un cola temporaria exclusiva para este consumidor (búzon de correos)
result = channel.queue_declare(queue="basedatos", exclusive=True, durable=True)
queue_name = result.method.queue

#La cola se asigna a un 'exchange'
channel.queue_bind(exchange='nestor', queue=queue_name, routing_key="basedatos")


##########################################################


########## ESPERA Y GUARDA EN LA BD CUANDO RECIBE UN MENSAJE ####

# print(' Nestor_Translate_Es_En Waiting for messages...')

def callback(ch, method, properties, body):
    query = str(body)
    print(query)
    sql = "INSERT INTO mensajes (texto) VALUES ("+query+")"
    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

    ########## PUBLICA EL RESULTADO COMO EVENTO EN RABBITMQ ##########
    channel.basic_publish(exchange='nestor', routing_key="publicar_slack", body="Este mensaje fue guardado: "+query[0:8]+"...")


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

###########################################################