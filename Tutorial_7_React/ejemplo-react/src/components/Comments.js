import React from 'react';
import Comment from './Comment'

class Comments extends React.Component {
    render() {
        return <div style={commentsStyle}>
            <h1>Comentarios:</h1>
            {this.props.com.map(e => <Comment key={e.author} com={e} />)}
        </div>
    }
}

const commentsStyle = {
    color: 'red'
}

export default Comments;