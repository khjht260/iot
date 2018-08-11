import React, { Component } from 'react';


// const payload = {
//   username: "khjht260",
//   password: "650103"
// }
const payload = {
  username: "1051516",
  password: "khjh25263"
}

class SignInComp extends Component {
  render() {
    if (this.props.permission) return <div></div>
    return (
      <div>
        <input class="css-input"
          id="username-input" 
          placeholder="帳號：例如1072003"
          autoFocus
          defaultValue={payload.username}
        />
        <input class="css-input"
          type="password" 
          id="password-input"
          placeholder="密碼：khjh加身分證末五碼" 
          defaultValue={payload.password}
        />
        <button className="myButton"
          onClick={this.props.handleSignIn} 
        > 確認 </button>
      </div>
    );
  }
}

export default SignInComp;