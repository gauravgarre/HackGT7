import React, { Component } from "react";
import Axios from "Axios";

export default class SignUp extends Component {
  constructor (props){
    super(props)
    this.state ={

    }
  }
  render() {
      return (
          <form>
              <h3>Sign Up</h3>

              <div className="form-group">
                  <label>First name</label>
                  <input type="text" className="form-control" placeholder="First name" />
              </div>

              <div className="form-group">
                  <label>Last name</label>
                  <input type="text" className="form-control" placeholder="Last name" />
              </div>

              <div className="form-group">
                  <label>Username</label>
                  <input type="text" className="form-control" placeholder="Enter username" />
              </div>

              <div className="form-group">
                  <label>Password</label>
                  <input type="password" className="form-control" placeholder="Enter password" />
              </div>

              <button type="submit" className="btn btn-primary btn-block">Sign Up</button>
              <p className="forgot-password text-right">
                  Already registered <a href="http://localhost:3000/sign-in">sign in?</a>
              </p>
          </form>
      );
  }
}
