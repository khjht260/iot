import React, { Component } from 'react';


const payload = {
  username: "khjht260",
  password: "650103"
}

class SignInComp extends Component {
  render() {
    if (this.props.permission) return <div></div>
    return (
      <div>
        <input 
          id="username-input" 
          placeholder="username"
          autoFocus
          defaultValue={payload.username}
        />
        <input
          type="password" 
          id="password-input"
          placeholder="password" 
          defaultValue={payload.password}
        />
        <button 
          onClick={this.props.handleSignIn} 
        > SIGN IN </button>
      </div>
    );
  }
}

export default SignInComp;