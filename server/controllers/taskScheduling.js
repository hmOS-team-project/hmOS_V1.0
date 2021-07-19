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
    Task.find({ "taskStatus": 'Unexecuted' }, function(err, result) {
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
            hostname: '127.0.0.1',
            port: 5001,
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
                    Task.findByIdAndUpdate(executingTask._id, { "resultUrl": tempTask.queryUrl }, function(err, result) {})
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