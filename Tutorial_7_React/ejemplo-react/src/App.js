import React from 'react';
import './App.css';
import comments from './sample/comments.json'

import Comments from './components/Comments'
import CommentForm from './components/CommentForm';

class App extends React.Component {

  state = {
    comments: comments
  }

  render() {
    return <div>
      <Comments com={this.state.comments} />
      <CommentForm />
    </div>
  }
}

export default App;
