const mongoose = require('mongoose')

const schema = new mongoose.Schema({
        //用户id
        userId: { type: Number, require: true },
        //任务名字
        taskName: { type: String },
        //时间要求
        taskTimeRequire: { type: String },
        //精度要求
        taskAccRequire: { type: Number },
        //描述
        description: { type: String, require: true },
        //创建时间
        startTime: { type: Date },
        //资源是否自定义
        resourceIsCustom: { type: Array },
        //模型搭建
        modelIsCustom: { type: Array },
        //协作模式
        comodeIsCustom: { type: Array },
        //任务状态（三种） Unexecuted，executing，Finished
        taskStatus: { type: String, enum: ['Unexecuted', 'Executing', 'Finished'] },
        //任务类型(四种) Classification，Identification，Generation，Others
        taskTpye: { type: String, enum: ['Classification', 'Identification', 'Generation', 'Others'] },
        //行人照片路径
        queryUrl: { type: String },
        //数据集路径
        videoUrl: { type: String },
        //结果路径
        resultUrl: { type: String },
        //作者
        // author: { type: mongoose.SchemaTypes.ObjectId, ref: 'User' }
    })
    //导出model模块
module.exports = mongoose.model('task', schema)