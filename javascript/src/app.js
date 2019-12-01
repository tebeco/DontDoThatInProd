const express = require('express')
const app = express()

app.get('/', function (req, res) {
  res.send('Hello World from js!')
})

app.listen(3000, "0.0.0.0", function () {
  console.log('Example app listening on port 3000!')
})
