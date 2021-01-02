import React from 'react';
import Comment from './Comment'

class Comments extends React.Component {
    render() {
        return <div>
            <h1>Comentarios:</h1>
            {this.props.com.map(e => <Comment key={e.author} com={e} />)}
        </div>
    }
}

export default Comments;