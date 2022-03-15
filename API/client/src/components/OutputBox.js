import React from 'react';

class OutputBox extends React.Component {
    
    render(){
      let result  = this.props.result;
      let prediction = result.slice(0,9)
      let newsStr  = result.slice(9)
      let newsIn = newsStr.split("`")
        return(

            <div>
              This is the result : {prediction}
              {newsIn.map((item,i)=>{
                return <div key={i}> {item} </div>
              })}
              
            </div>)
        }
}

export default OutputBox;
