//添加引用
let OSS = require('ali-oss')
let express = require('express')
let app = express()
var bodyParser = require('body-parser')
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
var cors = require('cors');
app.use(cors());
let multer = require('multer')
var multiparty = require("multiparty");
//允许跨域 视情况而定
// app.all('*', function(req, res, next) {
//         res.header('Access-Control-Allow-Origin', '*')
//         res.header('Access-Control-Allow-Headers', 'X-Requested-With,Content-Type,X-Token')
//         res.header('Access-Control-Allow-Methods', 'PUT,POST,GET,DELETE,OPTIONS')
//         res.header('Content-Type', 'application/json;charset=utf-8')
//         next()
//     })
//存储点 放置在和app.js同级的uploads目录下
let storage = multer.diskStorage({
    destination: function(req, file, cb) {
        cb(null, './uploads')
    },
    //上传的文件以 时间(毫秒级) + 原来的名字命名
    filename: function(req, file, cb) {
        cb(null, Date.now() + '-' + file.originalname)
    }
})

//创建multer对象 设置文件大小上限为1GB fileFilter 对文件进行筛选 比如文件扩展名等
let upload = multer({
        storage: storage,
        limits: { fileSize: 1024 * 1024 * 1024 },
        fileFilter: function(req, file, cb) {
            console.log(file)
            cb(null, true)
        }
    })
    //传输单个文件的配置
let uploadSingle = upload.single('image')
    //post接口用上面的函数对象处理
app.post('/upload/single', upload.single('file'), (req, res) => {
    uploadSingle(req, res, (err) => {
        if (err instanceof multer.MulterError) {
            console.log(err)
            res.json({
                code: '405',
                type: 'single',
                error: 'multer error'
            })
        } else if (err) {
            console.log(err)
            res.json({
                code: '402',
                type: 'single',
                error: 'unknown error'
            })
        } else {
            put(req.file.filename) //这个put函数为向阿里云oss上传文件的函数
            res.json({
                code: '200',
                type: 'single',
                originalname: req.file.filename
            })

        }
    })
})
app.post('/download/single', (req, res) => {
    listDir('Feedback/').then((result) => {
        url = client.signatureUrl(result.objects[1].name);
        console.log(url);
        res.json({
            code: '200',
            type: 'single',
            url: url
        })
    });
})
app.post('/download/getResult', (req, res) => {
    url = client.signatureUrl('Result/' + req.body.resulturl);
    console.log(url);
    res.json({
        code: '200',
        type: 'single',
        resulturl: url
    })
})
app.post('/download/getquery', (req, res) => {
    url = client.signatureUrl('query/' + req.body.queryurl);
    console.log(url);
    res.json({
        code: '200',
        type: 'single',
        queryUrl: url
    })
})
app.post('/submitlabel', (req, res) => {
    let label = req.body.label
    listDir('Feedback/').then((result) => {
        client.copy('CompletedTask/' + Date.now() + '-' + result.objects[1].name + '-' + label, result.objects[1].name)
        client.delete(result.objects[1].name).then(
            (result) => {

                res.json({
                    code: '200',
                    type: 'single',
                    url: url
                })
            }
        );
    });
})
let client = new OSS({
    region: 'oss-cn-beijing', //阿里云对象存储地域名
    accessKeyId: 'LTAI5tDnntNGV1YkT6kofCwe', //api接口id
    accessKeySecret: '69ZyWLP0u74N1aix3VPNfwC2yWVNdW', //api接口密码
})

client.useBucket('npu-hmos1') //使用的存储桶名
    //向存储桶中添加文件的接口
async function put(filename) {
    console.log(filename)
    try {
        console.log(filename)
        let result = await client.put('query/' + filename, 'uploads/' + filename)
        console.log(result) //在此处记录 url name 等信息
    } catch (err) {
        console.log(err)
    }
}
async function listDir(dir) {
    try {
        let result = await client.list({
            "max-keys": 5,
            prefix: dir,
            delimiter: '/'
        });
        return result
    } catch (e) {
        console.log(e);
    }
}
//监听端口 接收post信息
let server = app.listen(2333, function() {
    const port = server.address().port
    console.log('监听端口：%s', port)
})