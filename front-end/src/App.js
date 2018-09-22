import React, { Component } from 'react';
import './App.css';


class App extends Component {
  render() {
    return (
      <div>
        
        <form class="login">
        <h1 class="login-title"><strong>NICOBOT</strong></h1>
        <input type="text" class="login-input" placeholder="Email Adress" autofocus />
        <input type="password" class="login-input" placeholder="Password" />
        <input type="submit" value="Lets Go" class="login-button" />
        <p class="login-lost"><a href="">Forgot Password?</a></p>
        </form>
       </div>
    );
  }
}

export default App;
