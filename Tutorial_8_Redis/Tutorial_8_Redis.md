# Tutorial de Redis
### Autor: Simón Vergara

Tutorial Jeison Peguero: https://youtu.be/GU6N8Qk2dBE

## Introducción

Redis es un sistema de gestión de base de datos no relacional de código abierto,
que está basada en key-value (clave-valor) y almacena datos en memoria flexible,
es utilizado tanto de base de datos como de caché. Redis admite varios tipos de
datos como strings, listas, conjuntos, mapa de bits, entre otros.

Consiste en dos procesos principales, que son el cliente y el servidor, estos
pueden estar en el mismo equipo o en diferentes máquinas. Algunas características
de redis son: velocidad, persistencia, operaciones atómicas, sharding,
portabilidad, etc. Es compatible con muchos lenguajes de programación como:
C, C++, C#, Dart, Go, Java, Javascript, php, python, entre otros.

En general se utiliza para almacenar pequeña información textual a la que se debe
acceder o modificar de forma rápida, ya que almacena los datos en memoria primaria
lo que hace que sea muy eficaz, pero no puede almacenar archivos muy grandes.

## Instalar Redis en Ubuntu

    ~$ sudo apt update
    ~$ sudo apt upgrade
    ~$ sudo apt install build-essential tcl #Opcional! a veces no se requiere
    ~$ sudo apt install redis-server
    ~$ sudo apt install redis-tools