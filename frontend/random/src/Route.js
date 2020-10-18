import React, { Component } from 'react'
import {BrowseRouter as Router, Route, Switch, Link, Redirect} from "react-router-dom";
import MainPage from "./pages";
import NotFoundPage from "./pages/404";

class App extends Component{
  render(){
    return(
      <Router>
      <Switch>
        <Route exact path="/" component = {MainPage} />
        <Route exact path = "/404" component = {NotFoundPage} />
        <Redirect to = "/404"/>
      </Switch>
      </Router>

    )
  }
}
