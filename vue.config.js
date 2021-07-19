const webpack = require("webpack");
module.exports = {
    // baseUrl: './',
    assetsDir: 'static',
    productionSourceMap: false,
    configureWebpack: {
        plugins: [
            new webpack.ProvidePlugin({
                $: "jquery",
                jQuery: "jquery",
                jquery: "jquery",
                "window.jQuery": "jquery"
            })
        ]
    },

    // devServer: {
    //     host: 'localhost', // 本地主机
    //     port: 8081, // 端口号的配置
    //     https: false,
    //     proxy: { //配置跨域
    //         '/api': {
    //             target: 'http://localhost:3000/',
    //             changeOrigin: true, //允许跨域
    //             ws: true,
    //             // pathRewrite: {
    //             //     '/api': ''
    //             // }
    //         }
    //     }
    // }
}