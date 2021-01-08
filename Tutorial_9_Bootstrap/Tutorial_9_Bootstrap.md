# Tutorial de Bootstrap en React

### Autor: Simón Vergara

React Bootstrap: https://react-bootstrap.github.io/

Tutorial Adrian Twarog: https://youtu.be/8pKjULHzs0s

Bootstrap es un framework de front-end para hacer mucho más facil el desarrollo
de aplicaciones web, incluye muchos templates de fonts, botones, navegaciones,
carruseles, entre muchos otros componentes basados en HTML Y CSS. Con Bootstrap
se pueden crear aplicaciones responsive para que se adapten a cuaquier dispositivo.
También es compatible con todos los navegadores modernos.

En este tutorial explicaremos como añadir bootstrap a un proyecto React, cómo
implementar un componente y cómo ordenar la vista de la aplicación con los grids.

NOTA: Sólo explicaré los conceptos técnicos vistos desde lejos y con ejemplos
básicos, para mayor exactitud visitar la [documentación](https://react-bootstrap.github.io/)

## Implementar bootstrap en un proyecto React

Para mostrar las funcionalidades de bootstrap usaré el proyecto de react del 
Tutorial_7_React, que consiste en una aplicación web muy simple. Para implementar
Bootstrap un un proyecto react se puede hacer con yarn o bien npm:

    $ yarn add bootstrap react-bootstrap

Esto agregará los archivos de bootstrap a la carpeta node_modules.

A Continuación debemos importar las librerías de bootstrap en el archivo App.js:

    import 'bootstrap/dist/css/bootstrap.min.css';

Importando este css mínimo de bootstrap ya se generan cambios por ejemplo en la
tipografía.

## Usar componentes de bootstrap

Por ejemplo si queremos implementar una alerta, primero debemos importar Alert
desde react-bootstrap:

    import {Alert} from 'react-bootstrap'

Y para insertarla dentro de un React.Component, simplemente se escribe una etiqueta
Alert. Se le pueden pasar atributos (en este caso 'variant') para que cambie su
aspecto:

    <Alert variant="danger">Esto es una alerta de peligro!</Alert>

Para cada componente de react-bootstrap, hay una [documentación](https://react-bootstrap.github.io/components/alerts)
donde se puede ver cómo implementar cada uno. Todos los componentes se implementan
de una forma especial y bien explicada en la documentación.

## Grid system

Para hacer que la página sea responsive (adaptable a cualquier ancho) existe el
sistema de grid de bootstrap, que consiste en organizar la vista de la aplicación
en filas y columnas para separar los distintos componentes.

Para implementarlo primero se debe crear una etiqueta 'Container', que es un
espacio centrado de la página donde dentro de él irán las filas (rows) y columnas 
(col):

    <Container>
    <Row>
        <Col>1 of 2</Col>
        <Col>2 of 2</Col>
    </Row>
    <Row>
        <Col>1 of 3</Col>
        <Col>2 of 3</Col>
        <Col>3 of 3</Col>
    </Row>
    </Container>

De esta manera podemos organizar de muchas maneras los contenidos de la página,
[aquí] (https://react-bootstrap.github.io/layout/grid/) podrás ver distintas
maneras de asignar los espacios a las columnas para ajustar exactamente los
contenidos a nuestra intención sin perder la "responsidad".