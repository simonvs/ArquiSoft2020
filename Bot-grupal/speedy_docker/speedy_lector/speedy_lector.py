import pika
import sys
import time
import os
import logging
from pymongo import *
from flask import Flask
from slackeventsapi import SlackEventAdapter
from slack import WebClient


DATABASE = "speedy_mensajes"


def start_onboarding_text(channel: str, text: str):
    # Create a new onboarding tutorial.
    message = {
        "channel": channel,
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": text
                }
            }
        ]
    }
    slack_web_client.chat_postMessage(**message)
    #channel.basic_publish(exchange='speedy', routing_key="publicar_slack", body=text)


def get_doc(mensaje):
    doc = {
        "type": mensaje["type"],
        "text": mensaje["text"],
        "ts": mensaje["ts"]
    }
    return doc


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""

time.sleep(30)

############ CONEXION RABBITMQ ##############

HOST = os.environ['RABBITMQ_HOST']

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST))
channel = connection.channel()

#Creamos el exchange 'speedy' de tipo 'fanout'
channel.exchange_declare(exchange='speedy', exchange_type='topic', durable=True)


########### APLICACION WEB FLASK ############

# Initialize a Flask app to host the events adapter
app = Flask(__name__)

# Create an events adapter and register it to an endpoint in the slack app for event injestion.
slack_events_adapter = SlackEventAdapter(os.environ.get("SLACK_SIGNING_SECRET"), "/slack/events", app)

print(os.environ.get("SLACK_SIGNING_SECRET"))

# Initialize a Web API client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

print(os.environ.get("SLACK_TOKEN"))

client = MongoClient(host=os.environ['MONGO_HOST'], port=int(os.environ['MONGO_PORT']))
#databases = client.list_database_names()

#if DATABASE not in (databases):
    #db = client[DATABASE]
    #mensajes = slack_web_client.conversations_history(channel="#desarrollo")
    #for mensaje in mensajes['messages']:
    #    collection = db[mensaje['user']]
    #    doc = get_doc(mensaje)
    #    collection.insert_one(doc)

# An example of one of your Flask app's routes
@app.route("/")
def hello():
  return "Qué tal!"

@ slack_events_adapter.on("message")
def message(payload):
    #Inicio mongo
    client = MongoClient(host=os.environ.get("MONGO_HOST"), port=int(os.environ.get("MONGO_PORT")))
    db = client[DATABASE]

    #Obtención de evento
    event = payload.get("event", {})
    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")
    
    if text.startswith("!help"):
        mensaje = "Para saber el último mensaje de un usuario escriba: 'último mensaje de @user' \n Para saber la cantidad de mensajes de un usuario: 'cúantos mensajes ha enviado @user'"
        start_onboarding_text(channel_id,mensaje)
    #Ver si es alguna de las consultas de último mensaje o cuantos mensajes
    if "último mensaje" in text or "cúantos mensajes" in text:
        user = find_between(text, '@', '>')
        print("El usuario es este: ",user)
        collection = db[user]
        user_name = slack_web_client.users_info(user=user)['user']['name']
        if "último mensaje" in text:
            doc = collection.find().sort('ts', -1)
            texto = doc[0]['text']
            response = ("El último mensaje de @" + user_name + " es: " + texto)
        else:
            count = collection.find().count()
            response = ("La cantidad de mensajes de @" + user_name + " es: " + str(count))
        start_onboarding_text(channel_id, response)   
    #Si le dicen Hello, le contesta con Hola
    

    #Guarda el mensaje que recién llegó
    doc = get_doc(event)
    collection = db[user_id]
    collection.insert_one(doc)
    print("mensaje guardado!")

if __name__ == "__main__":
    # Create the logging object
    logger = logging.getLogger()

    # Set the log level to DEBUG. This will increase verbosity of logging messages
    logger.setLevel(logging.DEBUG)

    # Add the StreamHandler as a logging handler
    logger.addHandler(logging.StreamHandler())

    # Run our app on our externally facing IP address on port 3000 instead of
    # running it on localhost, which is traditional for development.
    app.run(host='0.0.0.0', port=3000)
