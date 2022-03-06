import React from "react";
import axios from 'axios';


class ImageInput extends React.Component{
    constructor(props){
        super(props);
        this.state = {image:null}
    }
    OnUpload=(event)=>{
        let reader = new FileReader()
        reader.readAsDataURL(event.target.files[0])
        reader.onload = e =>{
        this.setState({image:e.target.result})
        }
    }
    
    OnImageSubmit = (event)=>{
        event.preventDefault();
        // console.log(this.state.image)
        // axios.post('http://localhost:5000/submitImage/',this.state.image)
        // .then(res=>{console.log(res)})
        console.log(this.state.image.slice(23))
        this.DataFetcher(this.state.image)
    }

    DataFetcher = async(image)=>{
            const result = await fetch('http://localhost:5000/submitImage/',{
                method:"POST",
                headers:{
                    "Content-Type":"application/json"},
                    body:JSON.stringify({image})
                });
            const data = await result.json();
            console.log(data)
        } 
    render(){
    return(
            <div>
                <form>
                <input id ='fileItem' type="file" name="file" onChange={this.OnUpload} />
                <input type='submit' value='submit' onClick = {this.OnImageSubmit}/>
                </form>
            </div>
        )
    }
}

export default ImageInput;