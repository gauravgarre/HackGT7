import React from "react";

class App extends React.Component{

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

  render(){return(
    <div className = "container">
        <h1>What event would you like to add?</h1>
    <form>
      <input name = "eventName" type = "name" value = {this.state.eventName} onChange = {this.handleChange} placeholder = "Name of event" />
      <input name = "eventType" value = {this.state.eventType} onChange = {this.handleChange} placeholder = "Type" />
      <input name = "eventDate" type = "date" value = {this.state.eventDate} onChange = {this.handleChange} placeholder = "Due date" />
      <input name = "eventTime" type = "time" value = {this.state.eventTime} onChange = {this.handleChange} placeholder = "Estimated time" />
      <button>Submit</button>
    </form>
    </div>
  );
}
}
export default App;
