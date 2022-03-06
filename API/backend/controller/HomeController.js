const {spawn} = require("child_process");

module.exports = {
    normal: (req, res)=>{
        res.send('Hello');
    },
    submitText:(req,res)=>{
        console.log(req.body)
        let text =  req.body.text
            const childPython = spawn("C:/Users/samya/anaconda3/python.exe",['./controller/model_API.py',text])
            // childPython.stdout.setEncoding('utf8');
            childPython.stdout.on('data',(data)=>{
                console.log(`stdout':${data}`)
                res.send({"result": data.toString().replace(/(\r\n|\n|\r)/gm, "")})
            })
    
            childPython.stderr.on('data',(data)=>{
                console.error(`stderror:${data}`);
            })
    
            childPython.on('close',(code)=>{
                console.log(`child process exited with code ${code}`)
            })
            
    },
    submitImage:(req,res)=>{
        res.send('received')
        let image = req.body.image
            const childPython = spawn("C:/ProgramData/Anaconda3/python.exe",['./controller/imageConverter.py',image.slice(23)])
            // childPython.stdout.setEncoding('utf8');
            childPython.stdout.on('data',(data)=>{
                console.log(`stdout:${data}`)
                // res.send({"result": data.toString().replace(/(\r\n|\n|\r)/gm, "")})
            })
    
            childPython.stderr.on('data',(data)=>{
                console.error(`stderror:${data}`);
            })
    
            childPython.on('close',(code)=>{
                console.log(`child process exited with code ${code}`)
            })
    },
    
}