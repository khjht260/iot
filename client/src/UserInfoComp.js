import React, { Component } from 'react';


class SignInComp extends Component {
  render() {
    if (!this.props.permission) return <div></div>
    return (
      <div>
        <h3> credits: {this.props.data.credits}</h3>

        <button 
          id="activateBtn"
          onClick={this.props.handleActivate}
          disabled={!this.props.data.credits > 0}
        > ACTIVATE </button>

        <button
          onClick={this.props.handleSignOut}
        > SIGN OUT </button>
      </div>
    );
  }
}

export default SignInComp;