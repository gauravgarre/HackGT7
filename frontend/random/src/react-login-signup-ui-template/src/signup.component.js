import React, { Component } from "react";
const axios = require('axios');


class SignUp extends Component {
  constructor (props){
    super(props)
    this.state ={
      fName:"",
      lName:"",
      uName:"",
      pass:"",
      email:"",
      bday:"1000-01-01"
    }
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event){
    const name = event.target.name;
    this.setState({
      [name]: event.target.value
    })
  }

  createAxios(event){
        event.preventDefault();
        fetch('http://127.0.0.1:5000/login', {
           method: 'post',
           headers: {'Content-Type':'application/json'},
           body: JSON.stringify({
              firstName:this.state.fName,
              lastName:this.state.lName,
               username:this.state.uName,
               password:this.state.pass,
               email:this.state.email,
               birthDate:this.state.bday
           })
        }).then((data)=>{
          console.log(data)
        }).catch((e)=>{
          console.log(e)
        });
    };

  render() {
      return (
          <form>
              <h3>Sign Up</h3>

              <div className="form-group">
                  <label>First name</label>
                  <input type="text" name = "fName" value = {this.state.fName} onChange = {this.handleChange} className="form-control" placeholder="First name" />
              </div>

              <div className="form-group">
                  <label>Last name</label>
                  <input type="text" name = "lName" value = {this.state.lName} onChange = {this.handleChange} className="form-control" placeholder="Last name" />
              </div>

              <div className="form-group">
                  <label>Username</label>
                  <input type="text" name = "uName" value = {this.state.uName} onChange = {this.handleChange} className="form-control" placeholder="Username" />
              </div>

              <div className="form-group">
                  <label>Password</label>
                  <input type="password" name = "pass" value = {this.state.pass}  onChange = {this.handleChange} className="form-control" placeholder="Password" />
              </div>
              <div className="form-group">
                  <label>Email</label>
                  <input type="Email" name = "email" value = {this.state.email}  onChange = {this.handleChange} className="form-control" placeholder="Email" />
              </div>

              <button type="submit" onClick = {this.createAxios} className="btn btn-primary btn-block">Sign Up</button>
              <p className="forgot-password text-right">
                  Already registered <a href="http://localhost:3000/sign-in">sign in?</a>
              </p>
          </form>
      );
  }
}
export default SignUp;
