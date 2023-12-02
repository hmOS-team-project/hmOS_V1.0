const express = require('express');
const mongoose = require('mongoose');
var mysql = require('mysql');
var cors = require('cors');
app = express();
app.use(cors());
var bodyParser = require('body-parser')
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
const jwt = require('jsonwebtoken')
const { jwtKeys } = require('./plugins/mongodb')
const db = require('./plugins/mongodb').mongoURI
const task = require('./routes/task')
const user = require('./routes/user')
const cla_task = require('./routes/cla_task')
app.use(bodyParser.json())
// 连接数据库
mongoose.connect(db, { useNewUrlParser: true })
    .then(() => {
        console.log('mongodb connect success')
        //任务调度模块
        const taskScheduling = require('./controllers/taskScheduling')
    })
    .catch(err => { console.log(err) })
app.use(function (req, res, next) {
    if (req.path === '/api/user/login' || req.path === '/api/user/register') {
        next()
    } else {
        var token = req.body.token || req.query.token || req.headers['authorization']
        if (token) {
            // 解码 token (验证 secret 和检查有效期（exp）)
            jwt.verify(token, jwtKeys, function (err, decoded) {
                if (err) {
                    return res.status(401).json({ success: 0, message: '无效的token.' })
                } else {
                    // 如果验证通过，在req中写入解密结果
                    req.body.username = decoded.username
                    req.body.userId = decoded.id
                    next() // 继续下一步路由
                }
            })
        } else {
            // 没有拿到token 返回错误
            return res.status(401).json({
                success: 0,
                message: '没有找到token.'
            })
        }
    }
})
//任务路由
app.use('/api/task', task)
//用户路由
app.use('/api/user', user)
//分类任务路由
app.use('/api/cla_task', cla_task)
app.listen(3000, () => {
    console.log('http://localhost:3000');
})