import React ,{ Component }from 'react';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

class App extends Component{

constructor(props){
  super(props)
  this.state ={
    eventName : "",
    eventType : "",
    eventDate : "",
    eventTime : ""
  }
  this.handleChange = this.handleChange.bind(this);
}

  handleChange(event){
    const name = event.target.name;
    this.setState({
      [name]: event.target.value
    })
  }

render(){return (
  <form>
<div className = "container">
	<div class="form-group">
		<label for="eventName" class="control-label">Event Name</label>
		<input name = "eventName" type = "name" value = {this.state.eventName} onChange = {this.handleChange} placeholder = "Name of event" />
	</div>

	<div class="form-group">
		<label for="eventType" class="control-label">Event Type</label>
    <select class="form-control" id="eventType">
      <option>Assignments</option>
      <option>Tests</option>
      <option>Quizzes</option>
      <option>Others</option>
      </select>
	</div>

	<div class="form-group">
		<label for="street2_id" class="control-label">Due Date</label>
		<input name = "eventDate" type = "date" value = {this.state.eventDate} onChange = {this.handleChange} placeholder = "Due date" />
	</div>

	<div class="form-group">
		<label for="city_id" class="control-label">Estimated Time</label>
    <input name = "eventTime" type = "time" value = {this.state.eventTime} onChange = {this.handleChange} placeholder = "Estimated time" />
	</div>

	<div class="form-group">
		<button type="submit" class="btn btn-primary">Add to Calender</button>
	</div>
  </div>

</form>
);
}
}


export default App;
