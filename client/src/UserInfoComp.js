import React, { Component } from 'react';


class SignInComp extends Component {
  render() {
    const credits = this.props.data.num_progress - this.props.data.num_spent
    if (!this.props.permission) return <div></div>
    return (
      <div>
        <h3> {this.props.data.username} </h3>
        <h3> progress: {this.props.data.num_progress} </h3>
        <h3> spent   : {this.props.data.num_spent} </h3>
        <h3> credits : {credits}</h3>
        <button 
          id="activateBtn"
          onClick={this.props.handleActivate}
          disabled={!credits > 0}
        > ACTIVATE </button>

        <button
          onClick={this.props.handleSignOut}
        > SIGN OUT </button>
      </div>
    );
  }
}

export default SignInComp;