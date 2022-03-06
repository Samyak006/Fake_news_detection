const {spawn} = require("child_process");

// const childPython = spawn('python',['--version']);
const childPython = spawn('python',['model_API.py'])


childPython.stdout.on('data',(data)=>{
    console.log(`stdout':${data}`)
})

childPython.stderr.on('data',(data)=>{
    console.error(`stderror:${data}`);
})

childPython.on('close',(code)=>{
    console.log(`child process exited with code ${code}`)
})