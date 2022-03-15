// change the function to class based components
import React from 'react';
// import axios from 'axios';
import OutputBox from './OutputBox';
class TextInput extends React.Component{
    constructor(props){
        super(props);
        this.state = {entry:"",result:""}
    }
    OnTextSubmit=(event)=>{
        console.log(this.state.entry)
        event.preventDefault();
        this.DataFetcher(this.state.entry);
    }
    OnchangeText =(event)=>{
        this.setState({entry:event.target.value})
    }
    DataFetcher = async(text)=>{
        const result = await fetch('http://localhost:5000/submitText/',{
            method:"POST",
            headers:{
                "Content-Type":"application/json"},
                body:JSON.stringify({text})
            })
        const data = await result.json();
        console.log(data)
        this.setState({result:data.result})
    }
    render(){
        let Output;
        if (this.state.result !==""){
            Output = <OutputBox result ={this.state.result}/>
        }
    return(
        <div>
            <form method="POST">
            <input type='text' placeholder='Enter the text'onChange={this.OnchangeText} ></input>
            <input type='submit' value='submit' onClick={this.OnTextSubmit} />
            </form>
            {Output}
        </div>)}
}

export default TextInput;
