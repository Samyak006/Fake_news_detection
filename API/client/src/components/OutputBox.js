import React from 'react';

class OutputBox extends React.Component {
    render(){
        return(
            <div>
              THis is the result : {this.props.result}
            </div>)
        }
}

export default OutputBox;