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
        <el-row :gutter="24" style="margin: 30px 60px">
            <el-col :span="24">
                <el-card
                    shadow="hover"
                    style="height: 630px; padding: 5px; background-color: rgba(0, 168, 255, 0.2); border: 0"
                    :body-style="{ padding: '0px' }"
                >
                    <div class="header-box1">
                        <img src="../../assets/img/status.png" style="width: 45px; height: 45px" />
                        <span class="header-name">Computing Status</span>
                    </div>
                    <div class="divider div-transparent"></div>
                      <el-row :gutter="20">
            <el-col :span="12">
                <el-card shadow="hover" style="height: 285px; padding: 5px; background-color: rgba(0, 168, 255, 0.2); border: 0" 
                >
                        <div class="content-title">Task Accuracy</div>
                        <div class="schart" id="map"></div>
                </el-card>
            </el-col>
            <el-col :span="12">
                <el-card shadow="hover" style="height: 285px; padding: 5px; background-color: rgba(0, 168, 255, 0.2); border: 0" class="mgb20"
                  :body-style="{ padding: '15px' }" >
                        <div class="content-title">Task Progress</div>
                        <div class="schart" id="map2"></div>
                </el-card>
            </el-col>
        </el-row>
        <el-row :gutter="20">
            <el-col :span="12">
                <el-card shadow="hover" style="height: 285px; padding: 5px; background-color: rgba(0, 168, 255, 0.2); border: 0" >
                   <div class="content-title" style="margin-bottom:10px">Task Status</div>
                     <table class="table table-bordered">
                                    <tbody>
                                        <tr>
                                            <th scope="row">Current iterations:</th>
                                            <td>5 rounds</td>
                                              <th scope="row">Current computing mode:</th>
                                            <td>Parallel</td>
                                        </tr>
                                    </tbody>
                                </table>
                 <!-- <el-tag type="info" size="big" style="width:125px;height:40px;font-size:16px; margin-left:20px">当前迭代轮数:</el-tag>
                <el-tag type="info" size="big" style="width:115px;height:40px;font-size:16px;margin-left:20px">第五轮迭代</el-tag>
                     <el-tag type="info" size="big" style="width:125px;height:40px;font-size:16px; margin-left:20px">当前计算模式:</el-tag>
                    <el-tag type="info" size="big" style="width:125px;height:40px;font-size:16px; margin-left:20px">人机并行计算</el-tag> -->
                      <el-tag type="info" size="big" style="width:95px;height:60px;font-size:14px;font-weight:700;background:#03e9f4;border:0;color:white;text-align:center">Computing<br>Unit</el-tag>
              <el-progress type="circle" :percentage="22.2" style="margin-left:5px;" class="elprogress" :width="110"></el-progress>
              <div class="computing">
                  <span style="display:block">Human computing</span>
                  <img :src="url.url" style="height: 120px;width:120px">
                  </div>
              <el-progress type="circle" :percentage="40.2" style="margin-left:5px" class="elprogress" :width="110"></el-progress>
              <div class="computing">
                 <span style="display:block">Machine computing</span>
                  <img :src="url1.url1" style="height:120px;width:95px">
                  </div>
                </el-card>
            </el-col>
            <el-col :span="12">
                <el-card shadow="hover" style="height: 285px; padding: 5px; background-color: rgba(0, 168, 255, 0.2); border: 0" >
                       <div class="content-title" style="margin-bottom:10px">Current strategy</div>
                          <table class="table table-bordered" >
                                    <tbody>
                                        <tr>
                                            <th scope="row">Allocation Strategy:</th>
                                            <td>Default</td>
                                              <th scope="row">Fusion Strategy:</th>
                                            <td>Default</td>
                                        </tr>
                                    </tbody>
                                </table>
                    <div style="margin-top:20px">
                    <span class="description">Description</span>
                    <span class="description-content">Default allocation strategy means to assign video frame detection task to human and machine according to the set IOU threshold</span>
                    <br>
                     <span class="description" style="margin-top:10px">Description</span>
                    <span class="description-content" style="margin-top:10px">Default fusion strategy means to merge the human-machine calculation results according to the video frame number</span>
                            </div>
    <!-- <el-tag type="info" size="big" style="width:132px;height:40px;font-size:18px; margin-left:50px">当前分配策略:</el-tag>
                    <el-tag type="success" size="big" style="width:110px;height:40px;font-size:18px; margin-left:20px">分配策略一</el-tag>
                     <div class="description-box" style="margin-bottom:25px">
                    <span class="description">描述</span>
                    <span class="description-content">分配策略一表示按照设定的IOU阈值同时给人机分配检测视频帧任务</span>
                    </div>
    <el-tag type="info" size="big" style="width:132px;height:40px;font-size:18px; margin-left:50px">当前融合策略:</el-tag>
                    <el-tag type="success" size="big" style="width:110px;height:40px;font-size:18px; margin-left:20px">融合策略一</el-tag>
                    <div class="description-box">
                       <span class="description">描述</span>
                      <span class="description-content">融合策略一表示按照视频帧编号进行人机计算结果视频帧融合</span>
                      </div> -->
                </el-card>
            </el-col>
        </el-row>
                </el-card>
            </el-col>
        </el-row>
        <div class="copyrigntoutbox" style="position: relative; top: -22px">
            <span class="copyrigntmsg">Copyright © 2021 Northwestern Polytechnical University All Rights Reserved</span>
        </div>
    </div>
</template>
<script>
import '@/assets/css/style.css';
import '@/assets/css/normalize.min.css';
import '@/assets/css/Datacages_Homeindex.css';
import '@/assets/js/jquery.min.js.下载';
import '@/assets/js/jquery.js.下载';
import Schart from 'vue-schart';
import VueCropper from 'vue-cropperjs';
export default {
    data: function () {
          return {
            url: { url: require('../../assets/img/humanwork.gif') },
             url1: { url1: require('../../assets/img/robotwork.gif') },
            options2: {
                tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b}: {c} ({d}%)'
                },
                series: [
                    {
                        name: 'Total',
                        type: 'pie',
                        selectedMode: 'single',
                        radius: [0, '30%'],

                        label: {
                            position: 'inner'
                        },
                        labelLine: {
                            show: false
                        },
                        data: [
                            { value: 335, name: 'Completed'},
                            { value: 700, name: 'Incompleted' },
                        ]
                    },
                    {
                        name: 'Details',
                        type: 'pie',
                        radius: ['40%', '55%'],
                        label: {
                            formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                            backgroundColor: '#eee',
                            borderColor: '#aaa',
                            borderWidth: 1,
                            borderRadius: 4,
                            // shadowBlur:3,
                            // shadowOffsetX: 2,
                            // shadowOffsetY: 2,
                            // shadowColor: '#999',
                            // padding: [0, 7],
                            rich: {
                                a: {
                                    color: '#999',
                                    lineHeight: 22,
                                    align: 'center'
                                },
                                // abg: {
                                //     backgroundColor: '#333',
                                //     width: '100%',
                                //     align: 'right',
                                //     height: 22,
                                //     borderRadius: [4, 4, 0, 0]
                                // },
                                hr: {
                                    borderColor: '#aaa',
                                    width: '100%',
                                    borderWidth: 0.5,
                                    height: 0
                                },
                                b: {
                                    fontSize: 14,
                                    lineHeight: 33
                                },
                                per: {
                                    color: '#eee',
                                    backgroundColor: '#334455',
                                    padding: [2, 4],
                                    borderRadius: 2
                                }
                            }
                        },
                        data: [
                            { value: 235, name: 'Machine completed' },
                            { value: 100, name: 'Human completed' },
                            { value: 350, name: 'Machine incompleted' },
                            { value: 350, name: 'Human incompleted' },
                        ]
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

    methods: {
        taskmode() {
            this.$router.push('/taskmodeplus');
        },
                getMap() {
            var myChart = this.$echarts.init(document.getElementById('map'));
            let option = {
                xAxis: {
                    type: 'category',
                    // data: this.dataX,
                    data: ['Iteration 1', 'Iteration 2', 'Iteration 3', 'Iteration 4', 'Iteration 5'],
                    boundaryGap: false, //控制日期是否在中间显示
                    axisLabel: {
                        show: true, //是否显示日期
                        interval: 0, //强制显示全部 // rotate: 40,//倾斜的角度
                        textStyle: {
                            color: '#03e9f4', //日期的颜色
                            fontSize: 12 //字体的大小
                        }
                    },
                    axisLine: {
                        lineStyle: {
                            color: '#ccc' // x轴的颜色
                        }
                    }
                },
                yAxis: {
                    name: '(%)',
                    type: 'value',
                    axisLabel: {
                        formatter: '{value}',
                        textStyle: {
                            color: '#03e9f4' //数字的颜色
                        },
                        inside: false //控制数据是否在内侧还是外侧显示
                    },
                    axisLine: {
                        lineStyle: {
                            color: '#ccc' // 折线的颜色
                        }
                    }
                },
                series: [
                    {
                        // data: this.dataY,
                        data: [49.0, 71.2, 75.2, 84.5, 94.0],
                        type: 'line',
                        symbol: 'circle', //是否显示实心的折线圆点
                        smooth: true, //让折线有弧度
                        symbolSize: 7, //折线圆点的大小
                        itemStyle: {
                            normal: {
                                color: '#efc883', //折线点的颜色
                                lineStyle: {
                                    color: '#efc883' //折线的颜色
                                },
                                label: { show: true } //是否在折线点上显示数字
                            }
                        }
                    }
                ]
            };
            myChart.setOption(option);
        }
    },
    mounted() {
        this.getMap();
           var myChart = this.$echarts.init(document.getElementById('map2'));
           myChart.setOption(this.options2);
    },
};
</script>

<style scoped>
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
.grid-content {
    margin-top: 30px;
    display: flex;
    align-items: center;
    height: 40px;
}

.grid-num {
    font-size: 24px;
    font-weight: bold;
}

.grid-con-1 .grid-con-icon {
    background: rgb(45, 140, 240, 0);
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
    margin-left: 10px;
}
.header-name {
    color: rgb(0, 228, 255);
    margin-left: 20px;
    font-size: 24px;
    font-weight: 1000;
    cursor: pointer;
}
.divider {
    position: relative;
    margin-top: 5px;
    margin-bottom: 15px;
    height: 2px;
}
.div-transparent:before {
    content: '';
    position: absolute;
    top: 0;
    width: 100%;
    height: 1px;
    background-image: linear-gradient(to right, transparent, darkgrey, transparent);
}
.schart-box {
    display: inline-block;
    margin: 10px;
}
.schart {
    width: 665px;
    height: 250px;
}
.content-title {
    clear: both;
    font-weight: 400;
    line-height: 20px;
    font-size: 20px;
    color: #03e9f4;
}
.computing{
  margin-top:10px;
  display :inline-block;
  text-align: center;
  font-size:16px;
  color: white;
  font-weight:500;
}
.description{
      margin-right:20px;
      font-size:18px;
      color:#03e9f4;
      font-weight:600;

}
.description-box{
    margin-top:20px;
}
.elprogress>>>.el-progress__text{
    color:#03e9f4
}
            .table-bordered {
    border: 1px solid #dee2e6
}

.table-bordered td,
.table-bordered th {
    border: 1px solid #dee2e6
}
.table-bordered tr{
    /* background: transparent; */
    background:#03152E;
}
.table-bordered th{
    background:#03e9f4;
    color: white;
}
.table-bordered td{
       background:rgba(0, 168, 255, 0.2);
     color: #03e9f4;
     font-weight: 400;
}

.table-bordered thead td,
.table-bordered thead th {
    border-bottom-width: 2px
}
.table{
    margin-bottom: 0;
}
.description-content{
    color:white;
    font-weight:600
}
</style>