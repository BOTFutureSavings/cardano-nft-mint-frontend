const http = require("http");
const express = require('express');
const app = express();
const path = require('path')

const host = 'localhost';
const port = 8000;

// app.get('/', function (req, res) {
//     res.sendFile('index.html');
// });

app.use(express.static('.', path.dirname))

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
  })

  // Plug some rust in  https://blog.risingstack.com/how-to-use-rust-with-node-when-performance-matters/