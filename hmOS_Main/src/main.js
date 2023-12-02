import Vue from 'vue';
import App from './App.vue';
import router from './router';
import ElementUI from 'element-ui';
import VueI18n from 'vue-i18n';
import axios from 'axios'
import { messages } from './components/common/i18n';
import 'element-ui/lib/theme-chalk/index.css'; // 默认主题
// import './assets/css/theme-green/index.css'; // 浅绿色主题
import './assets/css/icon.css';
import './components/common/directives';
import 'babel-polyfill';
import "bootstrap"
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min'
import echarts from 'echarts'
import VueParticles from 'vue-particles'
import locale from 'element-ui/lib/locale/lang/en'
import Video from 'video.js'
import 'video.js/dist/video-js.css'

Vue.prototype.$video = Video
Vue.use(ElementUI, { locale })
Vue.prototype.$axios = axios
Vue.use(VueParticles)
Vue.prototype.$echarts = echarts
Vue.config.productionTip = false;
Vue.use(VueI18n);
Vue.use(ElementUI, {
    size: 'small'
});
const i18n = new VueI18n({
    locale: 'zh',
    messages
});
// http请求拦截
axios.interceptors.request.use(
        config => {
            if (localStorage.getItem('Authorization')) { // 判断是否存在token，如果存在的话，则每个http header都加上token
                config.headers.Authorization = localStorage.getItem('Authorization')
            }
            return config
        },
        err => {
            return Promise.reject(err)
        })
    // http响应拦截
axios.interceptors.response.use(
    response => {
        return response
    },
    err => {
        if (err.response) {
            switch (err.response.status) {
                case 401:
                    alert("The verification has expired. Please login again")
                        // 返回 401 清除token信息并跳转到登录页面
                    localStorage.removeItem('Authorization')
                    router.replace({
                        path: '/login'
                    })
            }
        }
        return Promise.reject(err) // 返回接口返回的错误信息
    })

new Vue({
    router,
    i18n,
    render: h => h(App)
}).$mount('#app');