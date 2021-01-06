# La biblia de Redis
### Autor: Simón Vergara

Tutorial Jeison Peguero: https://youtu.be/GU6N8Qk2dBE

Redis en python: https://realpython.com/python-redis/

# Introducción

Redis es un sistema de gestión de base de datos no relacional de código abierto,
que está basada en key-value (clave-valor) y almacena datos en memoria flexible,
es utilizado tanto de base de datos como de caché. Redis admite tipos de
datos como strings, listas, conjuntos, hashes, entre otros. En este tutorial
revisaremos los conceptos y comandos básicos de esta tecnología.

Consiste en dos procesos principales, que son el cliente y el servidor, estos
pueden estar en el mismo equipo o en diferentes máquinas. Algunas características
de redis son: velocidad, persistencia, operaciones atómicas, sharding,
portabilidad, etc. Es compatible con muchos lenguajes de programación como:
C, C++, C#, Dart, Go, Java, Javascript, php, python, entre otros.

En general se utiliza para almacenar pequeña información textual a la que se debe
acceder o modificar de forma rápida, ya que almacena los datos en memoria primaria
lo que hace que sea muy eficaz, pero no puede almacenar archivos muy grandes.

Para instalar redis en Ubuntu debería bastar con el comando:

    $ sudo apt install redis-server

Y para iniciar el servidor Redis está el comando redis-server y para el cliente
el comando redis-cli

# Configuración

El archivo de configuración de redis se encuentra en '/etc/redis/redis.conf'
(Ubuntu), que contiene todos los parámetros de configuración de Redis. Para
obtener y cambiar la configuración están los comandos CONFIG GET y CONFIG SET,
por ejemplo si queremos saber el directorio donde se está trabajando se tendría
que ejecutar:

    127.0.0.1:6379> config get dir
    1) "dir"
    2) "/home/simon"

Se pueden saber todos los parámetros con CONFIG GET *.

Para cambiar un parámetro se ejecuta el comando CONFIG SET {nombre} {valor}.
También podemos crear nuestro propio archivo de configuración, que se le tiene
que pasar al iniciar el servidor: redis-server /path/to/redis.conf

# Almacenando datos

A continuación se listan los tipos de datos que se pueden almacenar en Redis, junto
con sus comandos y un ejemplo. Recuerda que es una SGBD orientada a key-value, por
lo que cada dato debe tener asociada una clave o key para ser accedido.

## Strings

    SET {key} {value}
    GET {key}

Ejemplo:

    127.0.0.1:6379> set nombre simon
    OK
    127.0.0.1:6379> get nombre
    "simon"

## Hashes

Son una colección de pares clave-valor, para almacenar valores organizados por
campos.

    HMSET {key} {field} {value} {field} {value}...
    HMGET {key} {field} {field}...
    HGETALL {key}

Ejemplo: Crear un hash 'usuario.1' con los campos nombre, apellido y edad.

    127.0.0.1:6379> hmset usuario.1 nombre 'simon' apellido 'vergara' edad '22'
    OK
    127.0.0.1:6379> hmget usuario.1 nombre edad
    1) "simon"
    2) "22"
    127.0.0.1:6379> hgetall usuario.1
    1) "nombre"
    2) "simon"
    3) "apellido"
    4) "vergara"
    5) "edad"
    6) "22"

## Listas

En Redis las listas son un conjunto de strings ordenados por orden de inserción,
se le pueden agregar elementos tanto al principio como al final.

    LPUSH {key} {value} {value}...
    RPUSH {key} {value} {value}...
    LRANGE {key} {startIndex} {finalIndex}

Ejemplo:

    127.0.0.1:6379> lpush nombres simon matthieu tomas scarlett
    (integer) 4
    127.0.0.1:6379> lrange nombres 0 1
    1) "scarlett"
    2) "tomas"
    127.0.0.1:6379> lrange nombres 0 -1
    1) "scarlett"
    2) "tomas"
    3) "matthieu"
    4) "simon"

## Sets

Los sets o conjuntos se parecen a las listas, pero se diferencian en que los sets
no tienen un orden determinado y no se pueden insertar valores que ya existen.

    SADD {key} {member} {member}...
    SMEMBERS {key}

Ejemplo:

    127.0.0.1:6379> sadd telefonos 111 222 333
    (integer) 3
    127.0.0.1:6379> sadd telefonos 222
    (integer) 0
    127.0.0.1:6379> smembers telefonos
    1) "111"
    2) "222"
    3) "333"

## Sets Ordenados

Tienen el mismo comportamiento que los sets normales, por ejemplo que no se pueden
almacenar valores repetidos, pero en este caso los valores están ordenados respecto
al score de cada uno. Dos o más valores pueden tener el mismo score.

    ZADD {key} {score} {member} {score} {member} ...
    ZRANGEBYSCORE {key} {startScore} {endScore}
    
Ejemplo: En este ejemplo agregamos 4 números de teléfono con diferentes scores, y
después agregamos un quinto número con un score ya utilizado, de igual manera se 
guardan ambos datos. Pero esto no pasaría si tuviesen el mismo valor, solo se 
cambiaría el score.
    
    127.0.0.1:6379> zadd telefonos2 2 111 1 333 3 000 0 444
    (integer) 4
    127.0.0.1:6379> zrangebyscore telefonos2 0 3
    1) "444"
    2) "333"
    3) "111"
    4) "000"
    127.0.0.1:6379> zadd telefonos2 1 555
    (integer) 1
    127.0.0.1:6379> zrangebyscore telefonos2 0 3
    1) "444"
    2) "333"
    3) "555"
    4) "111"
    5) "000"

# Comandos para trabajar con keys

Para eliminar un valor según su key:

    DEL {key} {key} ...

Para serializar el valor de una key: (sirve para exportar valores sin problema)

    DUMP {key}

Para saber si una clave existe: (se le pueden pasar varias keys y retornará 
cuántas existen, no cuales)

    EXISTS {key} {key} ...

Para saber el nombre de las keys que siguen cierto patrón como nom* o *llido:
(retorna una lista de keys)

    KEYS {pattern}

Para establacer un tiempo en segundos para que un valor desaparezca:

    EXPIRE {key} {seconds}

Para establecer la fecha exacta de cuando el valor desaparecerá: (fecha en formato
timestamp)

    EXPIREAT {key} {timestamp}

Igual que el EXPIRE pero en milisegundos:

    PEXPIRE {key} {milliseconds}

Igual que EXPIREAT pero en milisegundos: (milisegundos en formato timestamp)

    PEXPIREAT {key} {milliseconds-timestamp}

Para hacer que un valor que tiene tiempo de expiración ya no lo tenga:
(inmortalizarlo)

    PERSIST {key}

Para saber el tiempo de expiración de una key en segundos: (si da negativo
quiere decir que ya fué eliminada)

    TTL {key}

Igual que TTL pero en milisegundos:

    PTTL {key}

Este comando retorna una key aleatoria entre las que existen:

    RANDOMKEY

Para renombrar una key:

    RENAME {key} {newKey}

Para renombrar una key sólo si el nuevo nombre no existe:

    RENAMENX {key} {newKey}

Para saber el tipo de dato:

    TYPE {key}

Para eliminar todos los datos de la BD: (¡PELIGROSO!)

    FLUSHDB

# Comandos para trabajar con Strings

Para obtener un substring desde ciertos índices: (empiezan desde el 0)

    GETRANGE {key} {stert} {end}

Para obtener el valor de una key y cambiar el valor al mismo tiempo:

    GETSET {key} {value}

Retorna una lista con los valores de las keys que se le den: (en el mismo orden)

    MGET {key} {key} ...

Para asignar un valor a una key durante ciertos segundos:

    SETEX {key} {seconds} {value}

Para asignar un valor a una clave siempre y cuando no exista:

    SETNX {key} {value}

Para cambiar el string a partir de cierto índice:

    SETRANGE {key} {offset} {value}

Para saber el largo de un string:

    STRLEN {key}

Para asignar múltiples valores y sus keys en un solo comando:

    MSET {key} {value} {key} {value} ...

Igual que el MSET pero lo asigna siempre y cuando la key no exista:

    MSETNX {key} {value} {key} {value} ...

Igual que el SETEX pero en milisegundos:

    PSETEX {key} {milliseconds} {value}

Para llevar un contador asignado a una key, cada vez que se invoca aumenta en 1:

    INCR {key}

Parecido al INCR pero se puede aumentar por más de uno:

    INCRBY {key} {increment}

Igual al INCRBY pero recibe un float en vez de un integer:

    INCRBYFLOAT {key} {increment}

Para reducir en uno el contador:

    DECR {key}

Para reducir por más de uno un contador:

    DECRBY {key} {decrement}

Para agregar o concatenar a un string existente:

    APPEND {key} {value}

# Comandos para trabajar con Hashes

Recordemos que los hashes son como registros, donde cada hash tiene una key
y varios campos (fields) con sus respectivos valores. Algunos comandos:

Para setear un hash:

    HMSET {key} {field} {value}

Para obtener todos los campos y valores de un hash:

    HGETALL {key}

Para ingresar sólo un campo en una clave:

    HSET {key} {field} {value}

Para ponerle un campo a un valor siempre y cuando no exista:

    HSETNX {key} {field} {value}

Lista todos los campos del hash, sin los valores:

    HKEYS {key}

Lista todos los values del hash, sin los campos:

    HVALS {key}

Para obtener el valor de un campo en ecpecífico de cierto hash:

    HGET {key} {field}

Para obtener todos los valores de los campos que le entreguemos:

    HMGET {key} {field} {field} ...

Para saber si un campo existe dentro de un hash:

    HEXISTS {key} {field}

Para eliminar uno o más campos de un hash:

    HDEL {key} {field} {field} ...

Para saber la cantidad de campos que tiene un hash:

    HLEN {key}

Para incrementar el valor entero de un campo hash, en el número que le demos:

    HINCRBY {key} {field} {increment}

Igual al HINCRBY pero con float:

    HINCRBYFLOAT {key} {field} {increment}

# Comandos para trabajar con listas

Para insertar valores al inicio o al final de la lista:

    RPUSH {key} {value} {value} ...
    LPUSH {key} {value} {value} ...

Para obtener los elementos desde {start} hasta {stop}: (índices desde el 0)

    LRANGE {key} {start} {stop}

Para agregar un valor a una lista siempre y cuando la lista exista:

    RPUSHX {key} {value}
    LPUSHX {key} {value}

Para saber la cantidad de elementos de la lista:

    LLEN {key}

Para acceder a un valor dado su índice: (desde el 0)

    LINDEX {key} {index}

Para insertar un valor antes o después de un valor dado:

    LINSERT {key} BEFORE|AFTER {pivot} {value}

Retorna el elemento del inicio o del fin y lo elimina de la lista:

    RPOP {key}
    LPOP {key}

Hace un RPOP desde la primera lista y la inserta al inicio de la segunda:
(retorna el valor)

    RPOPLPUSH {source} {destination}

Eliminará las primeras {count} ocurrencias de {value}:(count puede ser negativo
y eliminaría las últimas ocurrencias)

    LREM {key} {count} {value}

Para establacer el valor de una lista dado su índice:

    LSET {key} {index} {value}

Para recortar una lista dado cierto rango:

    LTRIM {key} {start} {stop}

Devuelve el primer o último valor de una serie de listas, y si no hay elementos,
entonces espera {timeout} segundos a que aparezca algún elemento:

    BLPOP {key} {key} ... {timeout}
    BRPOP {key} {key} ... {timeout}

Este último comando extrae el último elemento de la primera lista y lo inserta
al principio de la segunda: (lo retorna)

    BRPOPLPUSH {source} {destination} {timeout}


# Implementación en Python

Primero debemos importar redis con pip:

    $ python -m pip install redis

Después tenemos que asegurarnos de que el servidor esté operativo, ahi podemos
conectarnos de manera simple:

    >>> import redis
    >>> r = redis.Redis()
    >>> r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
    True
    >>> r.get("Bahamas")
    b'Nassau'

La clase principal es Redis() (linea 2), que puede ser llamada sin ningún
argumento, pero se le pueden poner varios argumentos si se necesitan:

    # From redis/client.py
    class Redis(object):
        def __init__(self, host='localhost', port=6379,
                     db=0, password=None, socket_timeout=None,
                     # ...