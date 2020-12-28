import React from 'react';
import './App.css';
import comments from './sample/comments.json'
import Comments from './components/Comments'

class App extends React.Component {

  state = {
    comments: comments
  }

  render() {
    return <div>
      <Comments com={this.state.comments} />
    </div>
  }
}

export default App;
