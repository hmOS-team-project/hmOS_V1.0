// 引入ali-oss
let OSS = require('ali-oss')
    /**
     *  [accessKeyId] {String}：通过阿里云控制台创建的AccessKey。
     *  [accessKeySecret] {String}：通过阿里云控制台创建的AccessSecret。
     *  [bucket] {String}：通过控制台或PutBucket创建的bucket。
     *  [region] {String}：bucket所在的区域， 默认oss-cn-hangzhou。
     */
export function client() { //data后端提供数据
    return new OSS({
        region: 'oss-cn-beijing', //阿里云对象存储地域名
        accessKeyId: 'LTAI5t5b19YVC88g9oL5bt7D', //api接口id
        accessKeySecret: 'g0HZd9eqRabSnyOxRbxd42rXvD8SQf', //api接口密码
        bucket: 'npu-hmos'
    })
}

/**
 * 生成随机文件名称
 * 规则八位随机字符，加下划线连接时间戳
 */
export const getFileNameUUID = () => {
    function rx() {
        return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1)
    }
    return `${+new Date()}_${rx()}${rx()}`
}