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