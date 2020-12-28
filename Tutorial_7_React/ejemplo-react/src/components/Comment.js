import React from 'react';

class Comment extends React.Component {
    render() {
        return <div>
            <h1> {this.props.com.author}</h1>
            <p>{this.props.com.text}</p>
        </div>
    }
}

export default Comment;