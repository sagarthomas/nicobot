const express = require('express');
const hbs = require('hbs');
const axios = require('axios');

const port = 3000;

var app = express();

//app.set('view engine', 'hbs');
// app.use(express.static(__dirname + '/public'));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/chat.html');
});

app.get('/chat', (req, res) => {
    var question = req.query.mytext;
    var config = {
        headers: {
            'Content-Length': 0,
            'Content-Type': 'text/plain'
        },
       responseType: 'text'
    };

    axios.post('https://mysterious-inlet-47286.herokuapp.com/send', question, config)
        .then((result) => {
            /*
            res.render('chat.hbs', {
                message: result.data
            });
            */
           res.send(result.data+"<div style=\"display: flex; justify-content: center; margin: 50px;\"><br><button onclick=\"location.href='./'\">Back</button></div>");
        })
        .catch((err) => {
            console.log(err);
        });
});


app.listen(port, () => {
    console.log(`Server is up on port ${port}`);
});
