const express = require('express');
const router = express.Router();
const db = require('../plugins/mysqldb');
const pwd = require('../libs/md5');
const jwt = require('jsonwebtoken')
const {
    jwtKeys
} = require('../plugins/mongodb')

//处理登录页面
router.post('/login', (req, res) => {
    var content = {
        username: req.body.username
    }
    db.query("select * from user where email=?", [req.body.email], function (err, result) {
        if (err) {
            res.json({
                success: 0
            })
        } else {
            if ("[]" != JSON.stringify(result)) {
                if (result[0].password === pwd.md5(req.body.password + pwd.MD5_SUFFIX)) { // 数据库密码加密，pwd
                    content.id = result[0].ID
                    content.email = result[0].email
                    content.username = result[0].username
                    content.credit = result[0].credit
                    content.ability = result[0].ability
                    content.position = result[0].position
                    content.isAdmin = result[0].isAdmin
                    res.json({
                        success: 1,
                        token: jwt.sign(content, jwtKeys, {
                            expiresIn: 24 * 60 * 60 * 1 // 1天过期
                        }),
                        //后续需要返回用户的基本信息，包括头像，任务完成情况等
                        // userName: user.userName,
                        // avatar: user.avatar
                    })
                } else {
                    res.json({
                        success: 0
                    })
                }
            } else {
                res.json({
                    success: 0
                })
            }
        }
    });
});

//处理注册页面
router.post('/register', (req, res) => {
    //1.获取表单提交的数据
    //2.操作数据库
    //   判断该用户是否存在，如果已存在，不允许注册；如果不存在，注册新建用户
    //3、发送响应
    var newUser = req.body
    db.query('SELECT * FROM user where email=?', [newUser.email], function (err, result) {
        if (err) {
            return res.status(500).json({
                success: false,
                message: 'Server err'
            })
        }
        if ("[]" != JSON.stringify(result)) {
            //邮箱已存在
            return res.status(200).json({
                status_code: 1,
                message: 'Email already exists.'
            })
        }
        //密码加密
        newUser.password = pwd.md5(newUser.password + pwd.MD5_SUFFIX)
        db.query('INSERT INTO user SET ?', newUser, function (err, result) {
            if (err) {
                res.status(500).json({
                    status_code: 500,
                    message: 'Server error'
                })
            }
            var content = {
                username: newUser.username,
                id: result.insertId,
                email: newUser.email,
                //一些默认信息
                credit: 50,
                ability: 50,
                position: 3
            }
            //注册成功
            res.status(200).json({
                status_code: 0,
                message: 'ok',
                token: jwt.sign(content, jwtKeys, {
                    expiresIn: 24 * 60 * 60 * 1 // 1天过期
                })
            })
        })
    })

});
//渲染用户编辑页面
router.get('/edit', function (req, res) {
    db.query('SELECT * FROM user WHERE ID=?', [req.body.userId], function (err, result) {
        if (err) {
            res.json({
                success: 0
            })
        } else {
            res.status(200).json({
                success: 1,
                user: result[0]
            })
        }
    })
})
//处理用户编辑页面
router.post('/edit', function (req, res) {
    db.query('UPDATE user SET username = ?,telephone = ?,address = ?,sex = ? WHERE ID = ?', [req.body.name, req.body.telephone, req.body.address, req.body.sex, req.body.userId], function (err, result) {
        if (err) {
            res.status(500).json({
                success: 0,
                message: 'Server error'
            })
        } else {
            var content = {
                username: req.body.name,
                id: req.body.userId,
                email: req.body.email
            }
            res.status(200).json({
                success: 1,
                token: jwt.sign(content, jwtKeys, {
                    expiresIn: 24 * 60 * 60 * 1 // 1天过期
                })
            })
        }
    })
})
//返回所有用户
router.get('/getalluser', function (req, res) {
    db.query('SELECT * FROM user ', function (err, result) {
        if (err) {
            res.json({
                success: 0
            })
        } else {
            res.status(200).json({
                success: 1,
                userList: result
            })
        }
    })
})
module.exports = router;