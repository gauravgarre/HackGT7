import React, { Component } from "react";

export default class Login extends Component {

  constructor (props){
    super(props)
    this.state ={
      uName:"",
      pass:""
    }
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event){
    const name = event.target.name;
    this.setState({
      [name]: event.target.value
    })
  }


  render() {
      return (
          <form>
              <h3>Sign In</h3>

              <div className="form-group">
                  <label>Username</label>
                  <input name = "uName" value = {this.state.uName} onChange = {this.handleChange} type="text" className="form-control" placeholder="Enter username" />
              </div>

              <div className="form-group">
                  <label>Password</label>
                  <input name = "pass" value = {this.state.pass} onChange = {this.handleChange} type="password" className="form-control" placeholder="Enter password" />
              </div>

              <button type="submit" className="btn btn-primary btn-block">Submit</button>

          </form>
      );
  }
}
