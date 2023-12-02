const Task = require("../models/task");
var http = require('http');
var querystring = require('querystring');
var bodyParser = require('body-parser')
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
console.log('task scheduling')
var tempTask
let machineAvailable = true
var updatestr = { "taskStatus": 'Executing' };
setInterval(function() {
    Task.find({ "taskStatus": 'Unexecuted', "queryUrl": { $ne: "" }, "videoUrl": { $ne: "" } }, function(err, result) {
        tempTask = result[0]
    })
}, 1000);
setInterval(function() {
    if (tempTask != undefined && machineAvailable && tempTask.queryUrl != '' && tempTask.videoUrl != '') {
        console.log(tempTask)
        executingTask = tempTask
        Task.findByIdAndUpdate(executingTask._id, updatestr, function(err, result) {})
        machineAvailable = false
        console.log(executingTask.taskName)
        var post_data = {}; //这是需要提交的数据
        var content = querystring.stringify(post_data);
        var options = {
            hostname: 'localhost',
            port: 8005,
            path: '/detect' + '/' + executingTask.queryUrl + '/' + executingTask.videoUrl,
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            }
        };
        var req = http.request(options, function(res) {
            machineAvailable = true
            res.setEncoding('utf8');
            res.on('data', function(chunk) {
                if (chunk === "success") {
                    Task.findByIdAndUpdate(executingTask._id, { "taskStatus": 'Finished' }, function(err, result) {})
                    Task.findByIdAndUpdate(executingTask._id, { "resultUrl": executingTask.videoUrl }, function(err, result) {})
                    Task.findByIdAndUpdate(executingTask._id, { "endTime": (new Date()).getTime() }, function(err, result) {})
                }
            });
        });
        req.on('error', function(e) {
            console.log('problem with request: ' + e.message);
        });
        // write data to request body
        req.write(content);
        req.end();
    }
}, 0);