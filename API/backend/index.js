const express = require('express');
const cors  =  require('cors');
const compression = require('compression');
const HomeRoutes = require('./routes/home');
const app = express();
app.use(express.json({limit: '50mb'}));
app.use(compression())
app.use(express.json())
app.use(cors())
app.use('/',HomeRoutes)

async function createUserConnection(){
    let connectionUrl = "mongodb://localhost:27017/"
    let db = await MongoClient.connect(connectionUrl,{ useUnifiedTopology: true });
    let dbo = db.db('FakeNews')
    return Promise.resolve(dbo);
}


app.listen(5000,()=>{
    console.log("server")
})

