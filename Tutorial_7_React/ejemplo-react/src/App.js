import React from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css';

import './App.css';
import comments from './sample/comments.json'

import Comments from './components/Comments'
import CommentForm from './components/CommentForm';
import Posts from './components/Posts'

class App extends React.Component {

	state = {
		comments: comments
	}

	addComment = (author, text) => {
		const newComment = {
			author: author,
			text: text
		}
		this.setState({
			comments: [...this.state.comments, newComment]
		})
	}

	render() {
		return <div>
			<Router>
				<Link to="/">Home</Link>
				<br />
				<Link to="/posts">Posts</Link>
				<Route exact path="/" render={() => {
					return <div>
						<CommentForm addComment={this.addComment} />
						<Comments com={this.state.comments} />
					</div>
				}}>
				</Route>

				<Route path="/posts" component={Posts} />

			</Router>
		</div>
	}
}

export default App;
