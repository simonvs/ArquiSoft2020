import React from 'react';
import Comment from './Comment'

class Comments extends React.Component {
    render() {
        return this.props.com.map(e => <Comment key={e.author} com={e} />)
    }
}

export default Comments;