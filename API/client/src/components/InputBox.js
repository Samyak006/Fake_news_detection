import React from "react";
import TextInput from "./TextInput";
import ImageInput from "./ImageInput";


class InputBox extends React.Component {
    render(){
        let comp;    
        if(this.props.user ==='text'){
            comp =  <TextInput/>
        }
        if(this.props.user ==='image'){
            comp = <ImageInput/>
        }
        return(<div>
            {comp}
            </div>)     
    }
}

export default InputBox;