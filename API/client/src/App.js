import React from 'react';
// import {BrowserRouter, Route, Routes} from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './components/Home';
import Footer from './components/Footer';

class App extends React.Component{

  render(){
    return(
      <div className='App'>
        <Navbar/>
        <Home/>
        <Footer/>
      </div>
      
    )
  }
}

export default App;