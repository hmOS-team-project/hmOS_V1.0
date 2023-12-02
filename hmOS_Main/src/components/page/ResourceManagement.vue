<template>
    <div>
         <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-folder-opened"></i> 资源管理</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <el-row :gutter="20">
            <el-col :span="12">
                <!-- <el-row :gutter="20" class="mgb20" >
                    <el-col :span="8">
                        <el-card shadow="hover" :body-style="{padding: '0px'}">
                            <div class="grid-content grid-con-1">
                                <i class="el-icon-s-order grid-con-icon"></i>
                                <div class="grid-cont-right">
                                    <div class="grid-num">任务输入</div>
                                </div>
                            </div>
                        </el-card>
                    </el-col>
                </el-row> -->
                <el-card shadow="hover" style="height: 312px" class="mgb20">
                    <div slot="header" class="clearfix">
                        <span @click="toAddResource">计算资源</span>
                    </div>
                    <div id="machine_resource" style="float: left; width: 275px; height: 200px"></div>
                    <div  style="float: left;width: 50px; height: 200px">
                       <i class="el-icon-s-platform grid-con-icon1"></i>
                              <i class="el-icon-s-platform grid-con-icon1"></i>
                                  <i class="el-icon-s-platform grid-con-icon1"></i>
                                      <i class="el-icon-s-platform grid-con-icon1"></i>
                                          <i class="el-icon-s-platform grid-con-icon1"></i>
                                              <i class="el-icon-s-platform grid-con-icon1"></i>
                                </div>
                    <div id="human_resource" style="float: left; width: 275px; height: 200px"></div>
                     <div  style="float: left;width: 50px; height: 200px">
                       <i class="el-icon-s-custom grid-con-icon1"></i>
                         <i class="el-icon-s-custom grid-con-icon1"></i>
                          <i class="el-icon-s-custom grid-con-icon1"></i>
                             <i class="el-icon-s-custom grid-con-icon1"></i>
                                <i class="el-icon-s-custom grid-con-icon1"></i>
                                    <i class="el-icon-s-custom grid-con-icon1"></i>
                                </div>
                </el-card>
                <el-card shadow="hover" style="height: 312px">
                    <div slot="header" class="clearfix">
                        <span>存储资源</span>
                    </div>
                    服务器硬盘（1T）
                    <el-progress :stroke-width="22" :percentage="70" color="#f1e05a"></el-progress>
                    云存储（10T）
                    <el-progress :stroke-width="22" :percentage="25" color="#42b983"></el-progress>
                    临时存储（300G）
                    <el-progress :stroke-width="22" :percentage="10" color="#42b983"></el-progress>
                </el-card>
            </el-col>
            <el-col :span="12">
                <el-card shadow="hover" style="height: 312px" class="mgb20">
                    <div slot="header" class="clearfix">
                        <span>带宽资源</span>
                        <!-- <el-button style="float: right; padding: 3px 0" type="text">添加</el-button> -->
                    </div>
                    <div id="internet_up_resource" style="float: left; width: 285px; height: 200px; margin-left: 50px"></div>
                    <div id="internet_down_resource" style="float: left; width: 285px; height: 200px; margin-left: 30px"></div>
                </el-card>
                <el-card shadow="hover" style="height: 312px">
                    <div slot="header" class="clearfix">
                        <span>感知资源</span>
                    </div>
                    <div class="grid-content grid-con-2">
                                <i class="el-icon-lx-camera grid-con-icon"></i>
                                <div class="grid-cont-right">
                                    <div class="grid-num">50</div>
                                    <div>外接摄像头数量</div>
                                </div>
                            </div>
                    <div class="grid-content grid-con-3">
                                <i class="el-icon-lx-camera grid-con-icon"></i>
                                <div class="grid-cont-right">
                                    <div class="grid-num">200</div>
                                    <div>其他感知设备数量</div>
                                </div>
                            </div>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import Schart from 'vue-schart';
import bus from '../common/bus';
import VueCropper from 'vue-cropperjs';
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
                    text: '实时上传带宽'
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
                    name:'Mbps',
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
                    text: '实时下载带宽'
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
                    name:'Mbps',
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
            this.$router.push('/resourceList')
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
                text: 'GPU占用情况', //主标题
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
                        { value: 80, name: '占用' },
                        { value: 20, name: '未连接' },
                        { value: 60, name: '空闲' }
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
                text: '人力占用情况', //主标题
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
                        { value: 335, name: '忙碌' },
                        { value: 310, name: '离线' },
                        { value: 234, name: '空闲' }
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

.user-info {
    display: flex;
    align-items: center;
    padding-bottom: 20px;
    border-bottom: 2px solid #ccc;
    margin-bottom: 20px;
}

.user-avator {
    width: 120px;
    height: 120px;
    border-radius: 50%;
}

.user-info-cont {
    padding-left: 50px;
    flex: 1;
    font-size: 14px;
    color: #999;
}

.user-info-cont div:first-child {
    font-size: 30px;
    color: #222;
}

.user-info-list {
    font-size: 14px;
    color: #999;
    line-height: 25px;
}

.user-info-list span {
    margin-left: 70px;
}

.mgb20 {
    margin-bottom: 20px;
}

.todo-item {
    font-size: 14px;
}

.todo-item-del {
    text-decoration: line-through;
    color: #999;
}

.schart {
    width: 100%;
    height: 300px;
}
.pre-img {
    width: 100px;
    height: 130px;
    background: #f8f8f8;
    border: 1px solid #eee;
    border-radius: 5px;
}
.crop-demo {
    float: left;
    margin-left: 80px;
    width: 260px;
}
.crop-demo-btn {
    position: relative;
    width: 100px;
    height: 40px;
    line-height: 40px;
    padding: 0 20px;
    margin-left: 5px;
    background-color: #409eff;
    color: #fff;
    font-size: 14px;
    border-radius: 4px;
    box-sizing: border-box;
}
.submit-crop-demo-btn {
    position: relative;
    width: 100px;
    height: 40px;
    line-height: 40px;
    padding: 0 20px;
    margin-left: 5px;
    margin-top: 10px;
    background-color: #409eff;
    color: #fff;
    font-size: 14px;
    border-radius: 4px;
    box-sizing: border-box;
}
.crop-input {
    position: absolute;
    width: 20px;
    height: 40px;
    left: 0;
    top: 0;
    opacity: 0;
    cursor: pointer;
}
.upload-demo {
    width: 360px;
    float: left;
}
.query_input {
    margin-left: 360px;
}
.crop-btn-box {
    margin-top: 18px;
    float: right;
}
.task-submit-box {
    margin-left: 150px;
}
.grid-con-icon1{
        font-size:28px;
}
</style>
