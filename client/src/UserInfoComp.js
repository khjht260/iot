import React, { Component } from 'react';


class SignInComp extends Component {
  render() {
    const credits = this.props.data.num_progress - this.props.data.num_spent
    if (!this.props.permission) return <div></div>
    return (
      <div>
        <h3> 帳號：{this.props.data.username}學霸幣總額: {this.props.data.num_progress*10} 元 已使用金額 : {this.props.data.num_spent*10}元</h3>
        <h3> </h3>
        <h3> </h3>
        <h3> 可使用金額 : {credits*10}元</h3>
        <h3> 按下下方投幣鍵，會扣10元學霸幣，玩籃球機一次，系統會自動幫你登出</h3>
        <h3> 若不想玩，按下方登出鍵登出，不會扣款</h3>
        <button className="myButton"
          id="activateBtn"
          onClick={this.props.handleActivate}
          disabled={!credits > 0}
        > 投  幣 </button>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

        <button className="myButton"
          onClick={this.props.handleSignOut}
        > 登  出 </button>
      </div>
    );
  }
}

export default SignInComp;