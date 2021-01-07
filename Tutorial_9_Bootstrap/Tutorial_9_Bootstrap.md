# Tutorial de Bootstrap 4

### Autor: Simón Vergara

Tutorial w3schools: https://www.w3schools.com/bootstrap4/

Curso Bootstrap FalconMasters: https://youtu.be/nug1pMke-y4

Bootstrap es un framework de front-end para hacer mucho más facil el desarrollo
de aplicaciones web, incluye muchos templates de fonts, botones, navegaciones,
carruseles, entre muchos otros componentes basados en HTML Y CSS. Con Bootstrap
se pueden crear aplicaciones responsive para que se adapten a cuaquier dispositivo.
También es compatible con todos los navegadores modernos.

En este tutorial explicaremos como añadir bootstrap a un proyecto. También veremos
algunos conveptos claves (no todos) como los grid, navbar, entre otros.

## Implementar bootstrap en un proyecto React

Para mostrar las funcionalidades de bootstrap usaré el proyecto de react del 
Tutorial_7_React, que consiste en una aplicación web muy simple. Para implementar
Bootstrap un un proyecto react se puede hacer con npm o bien con yarn:

    $ npm add bootstrap@next
    $ yarn add bootstrap

Esto agregará los archivos de bootstrap a la carpeta node_modules. Para poder usar
los componentes JavaScript se debe instalar también jquery:

    $ npm install jquery popper.js

A Continuación debemos importar las librerías de bootstrap y jquery en el archivo
index.js:

    import 'bootstrap/dist/css/bootstrap.min.css';

    import $ from 'jquery';
	import Popper from 'popper.js';
	import 'bootstrap/dist/js/bootstrap.bundle.min';