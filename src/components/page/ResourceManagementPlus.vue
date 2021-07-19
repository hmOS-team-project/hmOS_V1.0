<template>
    <div>
        <div id="loading" style="display: none">
            <div class="loadEffect">
                <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
            </div>
        </div>
        <!--标题栏-->
        <div class="Hometitlebox">
            <img src="../../assets/img/logo2.png" style="width: 50px; height: 50px; margin-right: 25px" />
            <a style="color: #00e4ff">hmOS1.0</a>
            <img src="../../assets/img/logo1.png" style="width: 60px; height: 50px; margin-left: 15px" />
        </div>
        <!--动效显示-->
        <!-- <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-folder-opened"></i> Resource Management</el-breadcrumb-item>
            </el-breadcrumb>
        </div> -->
        <el-row :gutter="20"   style="margin-top:50px">
            <el-col :span="12">
                <el-card shadow="hover" style="height: 312px; margin-left: 70px" class="mgb20">
                    <div slot="header" class="clearfix">
                        <span @click="toAddResource">Computing Resource</span>
                    </div>
                    <div id="machine_resource" style="float: left; width: 275px; height: 200px"></div>
                    <div style="float: left; width: 50px; height: 200px">
                        <i class="el-icon-s-platform grid-con-icon1"></i>
                        <i class="el-icon-s-platform grid-con-icon1"></i>
                        <i class="el-icon-s-platform grid-con-icon1"></i>
                        <i class="el-icon-s-platform grid-con-icon1"></i>
                        <i class="el-icon-s-platform grid-con-icon1"></i>
                        <i class="el-icon-s-platform grid-con-icon1"></i>
                    </div>
                    <div id="human_resource" style="float: left; width: 275px; height: 200px"></div>
                    <div style="float: left; width: 50px; height: 200px">
                        <i class="el-icon-s-custom grid-con-icon1"></i>
                        <i class="el-icon-s-custom grid-con-icon1"></i>
                        <i class="el-icon-s-custom grid-con-icon1"></i>
                        <i class="el-icon-s-custom grid-con-icon1"></i>
                        <i class="el-icon-s-custom grid-con-icon1"></i>
                        <i class="el-icon-s-custom grid-con-icon1"></i>
                    </div>
                </el-card>
                <el-card shadow="hover" style="height: 312px; margin-left: 70px">
                    <div slot="header" class="clearfix">
                        <span>Storage Resource</span>
                    </div>
                    Server Disk（1T）
                    <el-progress :stroke-width="22" :percentage="70" color="#f1e05a"></el-progress>
                    Cloud（10T）
                    <el-progress :stroke-width="22" :percentage="25" color="#42b983"></el-progress>
                    Cache（300G）
                    <el-progress :stroke-width="22" :percentage="10" color="#42b983"></el-progress>
                </el-card>
            </el-col>
            <el-col :span="12">
                <el-card shadow="hover" style="height: 312px; margin-right: 70px" class="mgb20">
                    <div slot="header" class="clearfix">
                        <span>Network Resource</span>
                        <!-- <el-button style="float: right; padding: 3px 0" type="text">添加</el-button> -->
                    </div>
                    <div id="internet_up_resource" style="float: left; width: 285px; height: 200px; margin-left: 50px"></div>
                    <div id="internet_down_resource" style="float: left; width: 285px; height: 200px; margin-left: 30px"></div>
                </el-card>
                <el-card shadow="hover" style="height: 312px; margin-right: 70px">
                    <div slot="header" class="clearfix">
                        <span>Perceived Resource</span>
                    </div>
                    <div class="grid-content grid-con-2">
                        <i class="el-icon-lx-camera grid-con-icon"></i>
                        <div class="grid-cont-right">
                            <div class="grid-num">50</div>
                            <div>number of webcam</div>
                        </div>
                    </div>
                    <div class="grid-content grid-con-3">
                        <i class="el-icon-lx-camera grid-con-icon"></i>
                        <div class="grid-cont-right">
                            <div class="grid-num">200</div>
                            <div>other devices</div>
                        </div>
                    </div>
                </el-card>
            </el-col>
        </el-row>

        <div class="copyrigntoutbox">
            <span class="copyrigntmsg">Copyright © 2020 Northwestern Polytechnical University All Rights Reserved</span>
        </div>
    </div>
</template>
<script>
import Schart from 'vue-schart';
import bus from '../common/bus';
import VueCropper from 'vue-cropperjs';
import '@/assets/css/style.css';
import '@/assets/css/normalize.min.css';
import '@/assets/js/index.js.下载';
import '@/assets/css/Datacages_Homeindex.css';
export default {
    name: 'dashboard',
    data: function () {
        return {
            name: localStorage.getItem('ms_username'),
            defaultSrc: require('../../assets/img/person.jpg'),
            fileList: [],
            imgSrc: '',
            cropImg: '',
            dialogVisible: false,
            oneDay: 24 * 3600 * 1000,
            form: {
                name: '',
                region: '',
                date1: '',
                date2: '',
                delivery: true,
                type: ['步步高'],
                resource: '小天才',
                desc: '',
                options: []
            },
            nowOptions: {
                visualMap: [
                    {
                        show: false,
                        type: 'continuous',
                        seriesIndex: 0,
                        min: 0,
                        max: 400
                    }
                ],
                title: {
                    left: 'center',
                    text: 'upload'
                },
                tooltip: {
                    trigger: 'axis',
                    formatter: function (params) {
                        params = params[0];
                        var date = new Date(params.name);
                        return date.getDate() + '/' + (date.getMonth() + 1) + '/' + date.getFullYear() + ' : ' + params.value[1];
                    },
                    axisPointer: {
                        animation: false
                    }
                },
                grid: {
                    top: '15%',
                    bottom: '10%'
                },
                xAxis: {
                    type: 'time',
                    splitLine: {
                        show: false
                    },
                    triggerEvent: true
                },
                yAxis: {
                    name: 'Mbps',
                    type: 'value',
                    boundaryGap: [0, '100%'],
                    max: 100,
                    splitLine: {
                        show: false
                    }
                },
                series: [
                    {
                        type: 'line',
                        showSymbol: false,
                        hoverAnimation: false,
                        data: []
                    }
                ]
            },
            nowOptions1: {
                visualMap: [
                    {
                        show: false,
                        type: 'continuous',
                        seriesIndex: 0,
                        min: 0,
                        max: 400
                    }
                ],
                title: {
                    left: 'center',
                    text: 'download'
                },
                tooltip: {
                    trigger: 'axis',
                    formatter: function (params) {
                        params = params[0];
                        var date = new Date(params.name);
                        return date.getDate() + '/' + (date.getMonth() + 1) + '/' + date.getFullYear() + ' : ' + params.value[1];
                    },
                    axisPointer: {
                        animation: false
                    }
                },
                grid: {
                    top: '15%',
                    bottom: '10%'
                },
                xAxis: {
                    type: 'time',
                    splitLine: {
                        show: false
                    },
                    triggerEvent: true
                },
                yAxis: {
                    name: 'Mbps',
                    type: 'value',
                    boundaryGap: [0, '100%'],
                    max: 100,
                    splitLine: {
                        show: false
                    }
                },
                series: [
                    {
                        type: 'line',
                        itemStyle: {
                            normal: {
                                lineStyle: {
                                    color: '#42b983'
                                }
                            }
                        },
                        showSymbol: false,
                        hoverAnimation: false,
                        data: []
                    }
                ]
            }
        };
    },
    components: {
        Schart,
        VueCropper
    },
    computed: {
        role() {
            return this.name === 'admin' ? '超级管理员' : '普通用户';
        }
    },
    // created() {
    //     this.handleListener();
    //     this.changeDate();
    // },
    // activated() {
    //     this.handleListener();
    // },
    // deactivated() {
    //     window.removeEventListener('resize', this.renderChart);
    //     bus.$off('collapse', this.handleBus);
    // },
    methods: {
        upChart() {
            let that = this;
            var data = [];
            var now = +new Date();
            var value = Math.random() * 1000;
            for (var i = 0; i < 60; i++) {
                now = new Date(+now + this.oneDay);
                data.push(this.randomData(now, value));
            }
            console.log(data[0].name);
            // 基于准备好的dom，初始化echarts实例
            var myChart = this.$echarts.init(document.getElementById('internet_up_resource'));
            // 绘制图表
            var temp = 59;
            let options = Object.assign(that.nowOptions, {});
            options.series.forEach((item) => {
                item.data = data;
                item.markPoint = {
                    data: [
                        [
                            {
                                symbol: 'none',
                                x: '95%'
                            },
                            {
                                symbol: 'circle',
                                name: '实时数据',
                                value: data[temp].value[1],
                                xAxis: data[temp].value[0]
                            }
                        ]
                    ]
                };
            });
            myChart.setOption(options);
            // 1秒定时器
            setInterval(() => {
                for (var i = 0; i < 1; i++) {
                    data.shift();
                    now = new Date(+now + this.oneDay);
                    data.push(this.randomData(now, value));
                }
                myChart.setOption(options);
            }, 1000);
        },
        downChart() {
            let that = this;
            var data = [];
            var now = +new Date();
            var value = Math.random() * 1000;
            for (var i = 0; i < 60; i++) {
                now = new Date(+now + this.oneDay);
                data.push(this.randomData(now, value));
            }
            console.log(data[0].name);
            // 基于准备好的dom，初始化echarts实例
            var myChart = this.$echarts.init(document.getElementById('internet_down_resource'));
            // 绘制图表
            var temp = 59;
            let options = Object.assign(that.nowOptions1, {});
            options.series.forEach((item) => {
                item.data = data;
                item.markPoint = {
                    data: [
                        [
                            {
                                symbol: 'none',
                                x: '95%'
                            },
                            {
                                symbol: 'circle',
                                name: '实时数据',
                                value: data[temp].value[1],
                                xAxis: data[temp].value[0]
                            }
                        ]
                    ]
                };
            });
            myChart.setOption(options);
            // 1秒定时器
            setInterval(() => {
                for (var i = 0; i < 1; i++) {
                    data.shift();
                    now = new Date(+now + this.oneDay);
                    data.push(this.randomData(now, value));
                }
                myChart.setOption(options);
            }, 1000);
        },
        randomData(now, value) {
            value = Math.random() * 100;
            var valueName =
                now.getFullYear() +
                '/' +
                (now.getMonth() + 1) +
                '/' +
                now.getDate() +
                ' ' +
                (now.getHours() >= 10 ? now.getHours() : '0' + now.getHours()) +
                ':' +
                (now.getMinutes() >= 10 ? now.getMinutes() : '0' + now.getMinutes()) +
                ':' +
                (now.getSeconds() >= 10 ? now.getSeconds() : '0' + now.getSeconds());
            return {
                name: now.toString(),
                value: [valueName, Math.round(value)]
            };
        },
        changeDate() {
            const now = new Date().getTime();
            this.data.forEach((item, index) => {
                const date = new Date(now - (6 - index) * 86400000);
                item.name = `${date.getFullYear()}/${date.getMonth() + 1}/${date.getDate()}`;
            });
        },
        setImage(e) {
            const file = e.target.files[0];
            if (!file.type.includes('image/')) {
                return;
            }
            const reader = new FileReader();
            reader.onload = (event) => {
                this.dialogVisible = true;
                this.imgSrc = event.target.result;
                this.$refs.cropper && this.$refs.cropper.replace(event.target.result);
            };
            reader.readAsDataURL(file);
        },
        cropImage() {
            this.cropImg = this.$refs.cropper.getCroppedCanvas().toDataURL();
        },
        cancelCrop() {
            this.dialogVisible = false;
            this.cropImg = this.defaultSrc;
        },
        imageuploaded(res) {
            console.log(res);
        },
        handleError() {
            this.$notify.error({
                title: '上传失败',
                message: '图片上传接口上传失败，可更改为自己的服务器接口'
            });
        },
        // 点击“计算资源”，发生页面跳转
        toAddResource() {
            this.$router.push('/resourceList');
        }
        // handleListener() {
        //     bus.$on('collapse', this.handleBus);
        //     // 调用renderChart方法对图表进行重新渲染
        //     window.addEventListener('resize', this.renderChart);
        // },
        // handleBus(msg) {
        //     setTimeout(() => {
        //         this.renderChart();
        //     }, 200);
        // },
        // renderChart() {
        //     this.$refs.bar.renderChart();
        //     this.$refs.line.renderChart();
        // }
    },

    created() {
        this.cropImg = this.defaultSrc;
    },
    mounted: function () {
        this.upChart();
        this.downChart();
        // 基于准备好的dom，初始化echarts实例
        var myChart1 = this.$echarts.init(document.getElementById('machine_resource'));
        // 绘制图表
        myChart1.setOption({
            title: {
                text: 'GPU Occupancy', //主标题
                x: 'center' //x轴方向对齐方式
            },
            tooltip: {
                trigger: 'item',
                formatter: '{a} <br/>{b} : {c} ({d}%)'
            },

            series: [
                {
                    name: '访问来源',
                    type: 'pie',
                    radius: '55%',
                    center: ['50%', '60%'],
                    data: [
                        { value: 80, name: 'Work' },
                        { value: 20, name: 'Offline' },
                        { value: 60, name: 'Idle' }
                    ],
                    itemStyle: {
                        emphasis: {
                            shadowBlur: 10,
                            shadowOffsetX: 0,
                            shadowColor: 'rgba(0, 0, 0, 0.5)'
                        }
                    }
                }
            ]
        });
        var myChart2 = this.$echarts.init(document.getElementById('human_resource'));
        // 绘制图表
        myChart2.setOption({
            title: {
                text: 'Human Occupancy', //主标题
                x: 'center' //x轴方向对齐方式
            },
            tooltip: {
                trigger: 'item',
                formatter: '{a} <br/>{b} : {c} ({d}%)'
            },
            series: [
                {
                    name: '访问来源',
                    type: 'pie',
                    radius: '55%',
                    center: ['50%', '60%'],
                    data: [
                        { value: 335, name: 'Busy' },
                        { value: 310, name: 'Offline' },
                        { value: 234, name: 'Idle' }
                    ],
                    itemStyle: {
                        emphasis: {
                            shadowBlur: 10,
                            shadowOffsetX: 0,
                            shadowColor: 'rgba(0, 0, 0, 0.5)'
                        }
                    }
                }
            ]
        });
    }
};
</script>

<style scoped>
.grid-content {
    display: flex;
    align-items: center;
    height: 80px;
}

.grid-cont-right {
    flex: 1;
    text-align: center;
    font-size: 14px;
    color: #999;
}

.grid-num {
    font-size: 24px;
    font-weight: bold;
}

.grid-con-icon {
    font-size: 24px;
    width: 40px;
    height: 40px;
    text-align: center;
    line-height: 40px;
    color: #fff;
}

.grid-con-1 .grid-con-icon {
    background: rgb(45, 140, 240);
}

.grid-con-1 .grid-num {
    color: rgb(45, 140, 240);
}

.grid-con-2 .grid-con-icon {
    background: rgb(100, 213, 114);
}

.grid-con-2 .grid-num {
    color: rgb(45, 140, 240);
}

.grid-con-3 .grid-con-icon {
    background: rgb(242, 94, 67);
}

.grid-con-3 .grid-num {
    color: rgb(242, 94, 67);
}
.loadEffect {
    width: 100px;
    height: 100px;
    position: relative;
    margin: 0 auto;
    top: 26%;
}

.loadEffect span {
    animation: load 1.04s ease infinite;
    display: inline-block;
    width: 30px;
    height: 10px;
    border-top-left-radius: 5px;
    border-bottom-left-radius: 5px;
    background: lightgreen;
    position: absolute;
}

.loadEffect span:nth-child(1) {
    left: 0;
    top: 50%;
    margin-top: -5px;
    animation-delay: 0.13s;
}

.loadEffect span:nth-child(2) {
    left: 10px;
    top: 20px;
    transform: rotate(45deg);
    animation-delay: 0.26s;
}

.loadEffect span:nth-child(3) {
    left: 50%;
    top: 10px;
    margin-left: -15px;
    transform: rotate(90deg);
    animation-delay: 0.39s;
}

.loadEffect span:nth-child(4) {
    top: 20px;
    right: 10px;
    transform: rotate(135deg);
    animation-delay: 0.52s;
}

.loadEffect span:nth-child(5) {
    right: 0;
    top: 50%;
    margin-top: -5px;
    transform: rotate(180deg);
    animation-delay: 0.65s;
}

.loadEffect span:nth-child(6) {
    right: 10px;
    bottom: 20px;
    transform: rotate(225deg);
    animation-delay: 0.78s;
}

.loadEffect span:nth-child(7) {
    bottom: 10px;
    left: 50%;
    margin-left: -15px;
    transform: rotate(270deg);
    animation-delay: 0.91s;
}

.loadEffect span:nth-child(8) {
    bottom: 20px;
    left: 10px;
    transform: rotate(315deg);
    animation-delay: 1.04s;
}

@keyframes load {
    0% {
        opacity: 1;
    }

    100% {
        opacity: 0.2;
    }
}
#loading {
    background-color: #181e20;
    opacity: 0.5;
    width: 100%;
    height: 100%;
    position: fixed;
    z-index: 999;
}
.progress {
    margin-top: 30px;
}

.down_span {
    color: #dfdede;
    font-size: 12px;
    font-weight: lighter;
}

h3,
ul,
li {
    margin: 0;
    padding: 0;
    list-style: none;
}

.box-content {
    color: #fff;
    text-align: center;
    width: 80%;
    height: 80%;
    transform: translateX(-50%) translateY(-50%) scale(1);
    position: absolute;
    left: 30%;
    top: 50%;
    z-index: 2;
    transition: all 0.3s ease 0.5s;
}

.content {
    opacity: 0;
    transform: translateX(-50%) translateY(-50%);
    position: absolute;
    left: 50%;
    top: 50%;
    z-index: 3;
    transition: all 0.3s ease 0s;
    overflow-y: hidden;
}

.post {
    color: #000;
    font-size: 13px;
    font-weight: 500;
    letter-spacing: 1px;
    text-transform: capitalize;
    display: inline-block;
    margin-bottom: 10px;
    opacity: 0;
    transform: translateY(-500px);
    transition: all 0.8s ease 0.15s;
}
.tile:hover .content {
    opacity: 1;
}
.tile:hover .title,
.tile:hover .post {
    opacity: 1;
    transform: translateY(0);
}
.title {
    color: #ff3a6f;
    font-size: 22px;
    font-weight: 600;
    text-transform: uppercase;
    transform: translateY(-500px);
    opacity: 0;
    transition: all 0.8s ease 0.3s;
}
</style>