const express = require('express')
const app = express()

app.use(express.json())
app.post('/team5/register', (req, res) => {
  console.log(req.body)
  team5data.forEach(element => {
    if (element.user_id === req.body.user_id) {
      res.send("이미 존재하는 아이디입니다.")
    }
  })
  team5data.push(req.body)
  res.send("확인이요")
})

app.get('/team5/login', (req, res) => {
  console.log("team5 login data:", team5data)
  res.send(team5data)
})

app.listen(3000)


let team5data = [
  {
    "user_id": "test",
    "user_pw": "test",
    "user_name": "test",
    "log": []
  }
];