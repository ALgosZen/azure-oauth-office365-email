const express = require('express')
const morgan = require('morgan')
const path = require('path')

const app = express()

const port = 3000
//configure morgan to log  requests
app.use(morgan('dev'))
//set frontend folder to serve public assets
app.use(express.static('JavaScriptSPA'))

app.get('*', function(req, res){
    res.sendFile(path.join(__dirname+'JavaScriptSPA/index.html'))
});

//start server
app.listen(port)
console.log('listening on port' + port+ '....')


