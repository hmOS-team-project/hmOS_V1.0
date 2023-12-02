const webpack = require("webpack");
// module.exports = {
//     // baseUrl: './',
//     assetsDir: 'static',
//     productionSourceMap: false,
//     configureWebpack: {
//         plugins: [
//             new webpack.ProvidePlugin({
//                 $: "jquery",
//                 jQuery: "jquery",
//                 jquery: "jquery",
//                 "window.jQuery": "jquery"
//             })
//         ]
//     },
// }
module.exports = {
    assetsDir: 'static',
    productionSourceMap: false,
    configureWebpack: (config) => {
        Object.assign(config, {
            plugins: [
                ...config.plugins,
                new webpack.ProvidePlugin({
                    jQuery: "jquery",
                    $: "jquery",
                    "windows.jQuery": "jquery"
                })
            ]
        });
        config.module.rules.push({
            test: /\.(html)$/,
            exclude: /(node_modules)/,
            use: [{
                loader: 'html-loader', // 解决ivew组件 忽略前缀i的问题
            }]
        })
    },
}