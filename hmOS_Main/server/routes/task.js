const express = require('express');

const router = express.Router()
const Task = require("../models/task");

//创建任务
router.post('/createtask', (req, res) => {
    Task.create(req.body, (err) => {
        if (err) return console.log(err)
        else {
            Task.find({
                "userId": req.body.userId,
                "startTime": req.body.startTime
            }, function (err, result) {
                if (err) {
                    res.json({
                        success: -1,
                    })
                } else {
                    res.json({
                        success: 1,
                        taskId: result[0]._id
                    })
                }
            })

        }
    })
})
//上传queryUrl
router.post('/queryUrl', async (req, res) => {
    var updatestr = { 'queryUrl': req.body.queryUrl };
    Task.findByIdAndUpdate(req.body.taskId, updatestr, function (err, result) {
        if (err) {
            res.json({
                success: -1,
            })
        } else {
            res.json({
                success: 1,
            })
        }
    })
})
//上传videoUrl
router.post('/videoUrl', async (req, res) => {
    var updatestr = { 'videoUrl': req.body.videoUrl };
    Task.findByIdAndUpdate(req.body.taskId, updatestr, function (err, result) {
        if (err) {
            res.json({
                success: -1,
            })
        } else {
            res.json({
                success: 1,
            })
        }
    })
})
router.get('/getalltask', async (req, res) => {
    Task.find({}, function (err, result) {
        if (err) {
            res.json({
                success: -1,
            })
        } else {
            res.json({
                success: 1,
                Tasklist: result
            })
        }
    })
})

router.post('/getmytask', async (req, res) => {

    var whereStr = { "userId": req.body.id };
    Task.find(whereStr, function (err, result) {

        if (err) {
            res.json({
                success: -1,
            })
        } else {
            res.json({
                success: 1,
                Tasklist: result
            })
        }
    })
})

router.post('/searchbystate', async (req, res) => {
    Task.find({
        "taskStatus": req.body.taskStatus,
    }, function (err, result) {
        if (err) {
            res.json({
                success: -1,
            })
        } else {
            res.json({
                success: 1,
                list: result
            })
        }
    })
})

router.post('/searchbydate', async (req, res) => {

    Task.find({
        "startTime": { $gte: new Date(req.body.startTime) }
    }, function (err, result) {

        if (err) {
            res.json({
                success: -1,
            })
        } else {
            res.json({
                success: 1,
                list: result
            })
        }
    })
})

router.post('/searchbydescription', async (req, res) => {

    Task.find({
        "description": { $regex: req.body.description },
    }, function (err, result) {

        if (err) {
            res.json({
                success: -1,
            })
        } else {
            res.json({
                success: 1,
                list: result
            })
        }
    })
})
router.post('/searchbyid', async (req, res) => {

    Task.find({
        "userId": req.body.userId,
    }, function (err, result) {

        if (err) {
            res.json({
                success: -1,
            })
        } else {
            res.json({
                success: 1,
                list: result
            })
        }
    })
})
router.post('/searchbytype', async (req, res) => {

    /*var taskName={"taskName":{ $regex: req.query.taskName }};
    var taskType={"taskType":req.query.taskType};
    var description={"description":{ $regex: req.query.description }};
    var startTime={"startTime":{$gte:new Date(req.query.startTime)}};
    */
    Task.find({
        //"taskName": { $regex: req.query.taskName },
        "taskType": req.body.taskType,
        // "description": { $regex: req.query.description },
        //"startTime": { $gte: new Date(req.query.startTime) }
    }, function (err, result) {

        if (err) {
            res.json({
                success: -1,
            })
        } else {
            res.json({
                success: 1,
                list: result
            })
        }
    })
})
// 更新资源
// router.put('/:id', async(req, res) => {
//         const model = await req.Model.findByIdAndUpdate(req.params.id, req.body)
//         res.send(model)
//     })
//     // 删除资源
// router.delete('/:id', async(req, res) => {
//         await req.Model.findByIdAndDelete(req.params.id)
//         res.send({
//             success: true
//         })
//     })
//     // 资源列表
// router.get('/', async(req, res) => {
//         const queryOptions = {}
//         const items = await req.Model.find().setOptions(queryOptions).limit(100)
//         res.send(items)
//     })
//     // 资源详情
// router.get('/:id', async(req, res) => {
//     const model = await req.Model.findById(req.params.id)
//     res.send(model)
// })

//中间件
// const resourceMiddleware = require('../../middleware/resource')
// app.use('/admin/api/rest/:resource', resourceMiddleware(), router)

module.exports = router