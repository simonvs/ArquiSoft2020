import React from 'react';

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

export default Comment;