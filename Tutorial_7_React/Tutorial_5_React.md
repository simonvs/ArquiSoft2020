# Tutorial de React JS
### Autor: Simón Vergara

Repositorio React: https://github.com/enaqx/awesome-react

Tutorial Fazt: https://www.youtube.com/watch?v=zIY87vU33aA&t=6027s&ab_channel=Fazt

Etiquetas HTML: https://www.mclibre.org/consultar/htmlcss/html/html-etiquetas.html


React es una librería de javascript para construir interfaces de usuario, fue desarrollada por facebook en 2013.
Es basada en componentes, que son partes reutilizables de la interfaz, y la implementación de un componente está muy simplificada.
En este tutorial revisaremos los conceptos básicos de React con pequeños ejemplos.


## Implementación de un componente

Para implementar un componente se puede hacer de varias formas, una de ellas es a través de una clase, que extiende a React.Component
y que debe devolver una etiqueta html, que sería lo que contiene el componente en sí

    import React from 'react';

    class Comment extends React.Component {
        render() {
            return <div>
                <p>Esto es un componente, que se puede reutilizar</p>
            </div>
        }
    }

    export default Comment;

## Props

Los props (propiedades) de un componente son los datos que se le pasan al ser invocados, por ejemplo en este caso al componente
"Comment" se le pasa el prop 'texto', que contiene el texto que se quiere imprimir.

Así se entregan los props:

    <Comment texto="Hola soy un comentario" />

Y se accede a ellos desde el componente con this.props:

    class Comment extends React.Component {
        render() {
            return <div>
                <p>{this.props.texto}</p>
            </div>
        }
    }

## State

El state o estado de un componente son los datos internos de cada componente, que pueden ser cambiados. Por ejemplo el componente
"Comment" tendrá en su state un booleano que se llame show que determina si se muestra o no:

    class Comment extends React.Component {

        state = {
            show: true
        }

        render() {
            if(this.state.show){
                return <div>
                    <h1> {this.props.com.author}</h1>
                    <p>{this.props.com.text}</p>
                </div>
            } else {
                return <p> No hay nada  </p>
            }
        }
    }

Este componente se tendría que invocar de la siguiente manera:

    <Comment author="Simon Vergara" texto="Esto es un comentario"/>

## Styles

Lo común al empezar a desarrollar en front-end es escribir aparte el archivo .css con todos los estilos ahi, lo que lo hace facil de
entender, pero escribiéndolos como funciones que retornan un objeto javascript se puede hacer que los estilos sean dinámicos, o sea que pueden cambiar
dependiendo del state o de los props por ejemplo:


    class Comment extends React.Component {

        state = {
            show: true
        }

        StyleComment() {
            return {
                color: this.state.show ? 'black' : 'white'
            }
        }

        render() {
            return <div style={this.StyleComment()}>
                <h2> {this.props.com.author}</h2>
                <p>{this.props.com.text}</p>
            </div>
        }
    }

También se podría agregar un estilo simplemente como un objeto de js:

    <div style={{color:'red'}}>

De esta misma manera se podrían poner muchas reglas de css para estilizar la interfaz, pero eso correspondería a un tutorial de CSS.

Tutorial CSS: https://www.w3schools.com/css/default.asp

## PropTypes

Los PropTypes sirven para declarar el tipo de dato que se espera de los props, 
sirve para generar código más robusto y correcto, en este ejemplo declaramos
los props que recibe "Comment", que sería 'author' y 'text':

    import React from 'react';
    import PropTypes from 'prop-types';

    class Comment extends React.Component {

        render() {
            return <div>
                <h2> {this.props.com.author}</h2>
                <p>{this.props.com.text}</p>
            </div>
        }
    }

    Comment.propTypes = {
        author: PropTypes.string.isRequired,
        text: PropTypes.string.isRequired
    }

NOTA: hay que importar la librería PropTypes al principio.

## Formularios o Forms

	import React from 'react';

	class CommentForm extends React.Component {

    	state = {
    		author: '',
 	    	text: ''
 	   }

 	   onSubmit = e => {
 	    	console.log(this.state)
 	    	e.preventDefault();
 	  	}

 	   	onChange = e => {
	    	console.log(e.target.name, e.target.value)
 	    	this.setState({
 	    		[e.target.name]: e.target.value
	    	})
	    }

		render() {
  	    	return (
   	        	<form onSubmit={this.onSubmit}>
   	            	<input
  	                	type="text"
   	            		name="author"
     	            	placeholder="Nombre: "
                 		onChange={this.onChange}
               	    	value={this.state.author} />
              		<br /> <br />
             		<textarea
              	    	name="text"
              	    	placeholder="Escribe un comentario: "
           	        	onChange={this.onChange}
            	    	value={this.state.text} />
            		<br /> <br />
            		<input type="submit" />
         		</form>
       		)
 	   	}
	}

export default CommentForm;