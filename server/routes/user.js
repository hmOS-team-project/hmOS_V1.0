const express = require('express');
const router = express.Router();
const db = require('../plugins/mysqldb');
const pwd = require('../libs/md5');
const jwt = require('jsonwebtoken')
const {
    jwtKeys
} = require('../plugins/mongodb')
router.post('/login', (req, res) => {
    var content = {
        username: req.body.username
    }
    db.query("select * from user where username=?", [req.body.username], function(err, result) {
        if (err) {
            res.json({
                success: 0
            })
        } else {
            if ("[]" != JSON.stringify(result)) {
                if (result[0].password === pwd.md5(req.body.password + pwd.MD5_SUFFIX)) { // 数据库密码加密，pwd
                    content.id = result[0].ID
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
module.exports = router;