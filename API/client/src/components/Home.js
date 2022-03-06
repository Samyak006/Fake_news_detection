import React from 'react';
import InputBox from './InputBox';

class Home extends React.Component{
    constructor(props){
        super(props);
        this.state = {value:""};
    }
    
    onChangeValue=(e)=>{
            this.setState({value:e.target.value})
    }

    render(){
        return(
        <div>
            <div>
            <label><input type='radio' value='text' name='input' onChange={this.onChangeValue} /> Text input </label>
            </div>
            <div>
            <input type='radio' value='image' name='input' onChange={this.onChangeValue}/> Image input
            </div>
            <InputBox user={this.state.value}/>
        </div>
        )}
}

export default Home;