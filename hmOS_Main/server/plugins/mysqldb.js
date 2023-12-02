var mysql = require('mysql');
// 创建一个数据库连接池
var pool = mysql.createPool({
    connectionLimit: 50,
    host: '127.0.0.1',
    user: 'root',
    password: 'root',
    database: 'localhmos'
});
// SELECT * FROM users
// 我们的方法支持两种模式
// 一种是只传入SQL语句和回调函数
// 一种是传入SQL语句、参数数据、回调函数
exports.query = function (sql, P, C) {
    var params = [];
    var callback;
    // 如果用户传入了两个参数，就是SQL和callback
    if (arguments.length == 2 && typeof arguments[1] == 'function') {
        callback = P;
    } else if (arguments.length == 3 && typeof arguments[2] == 'function') {
        params = P;
        callback = C;
    } else {
        throw new Error('对不起，参数个数不匹配或者参数类型错误');
    }
    // 如果用户传入了三个参数，那么就是SQL和参数数组、回调函数
    // 从池子里面拿一个可以使用的连接
    pool.getConnection(function (err, connection) {
        // Use the connection
        connection.query(sql, params, function () {
            // 使用完毕之后，将该连接释放回连接池
            connection.release();
            callback.apply(null, arguments);
        });
    });
};