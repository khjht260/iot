import React, { Component } from 'react';

import SignInComp from './SignInComp'
import UserInfoComp from './UserInfoComp'

import logo from './logo.svg';
import './App.css';


class App extends Component {
  state = {
    permission: false,
    credits: null,
    data: null,
  }

  handleSignIn = async () => {
    const usernameInput = document.getElementById('username-input')
    const passwordInput = document.getElementById('password-input')
    const payload = {
      username: usernameInput.value,
      password: passwordInput.value,
    }
    console.log(payload)
    const authStatus = await this.checkAuth(payload)
    console.log(authStatus)
    if (!authStatus.permission) {
      alert('permission denied')
      return
    }
    this.setState(authStatus)
  }
  checkAuth = (payload) => {
    return fetch('http://localhost:5000/checkAuth', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify(payload),
    })
    .then(res => res.json())
  }
  handleActivate = () => {
    fetch('http://localhost:5000/activate')
    this.handleSignOut()
  }
  handleSignOut = () => {
    this.setState({permission: false})
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        
        <SignInComp 
          permission={this.state.permission}
          handleSignIn={this.handleSignIn}  
        />
        <UserInfoComp
          permission={this.state.permission}
          data={this.state}
          handleActivate={this.handleActivate}
          handleSignOut={this.handleSignOut}
        />
      </div>
    );
  }
}

export default App;
