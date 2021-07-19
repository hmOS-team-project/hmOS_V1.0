<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item> <i class="el-icon-s-data"></i> 计算状态查看 </el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <el-row :gutter="20">
            <el-col :span="12">
                <el-card shadow="hover" style="height: 285px" class="mgb20">
                        <div class="content-title">任务执行精度</div>
                        <div class="schart" id="map"></div>
                </el-card>
            </el-col>
            <el-col :span="12">
                <el-card shadow="hover" style="height: 285px" class="mgb20" >
                        <div class="content-title">任务完成总进度</div>
                        <div class="schart" id="map2"></div>
                </el-card>
            </el-col>
        </el-row>
        <el-row :gutter="20">
            <el-col :span="12">
                <el-card shadow="hover" style="height: 285px" >
                   <div class="content-title" style="margin-bottom:30px">任务执行精度</div>
                 <el-tag type="info" size="big" style="width:125px;height:40px;font-size:16px; margin-left:20px">当前迭代轮数:</el-tag>
                <el-tag type="success" size="big" style="width:115px;height:40px;font-size:16px;margin-left:20px">第五轮迭代</el-tag>
                     <el-tag type="info" size="big" style="width:125px;height:40px;font-size:16px; margin-left:20px">当前计算模式:</el-tag>
                    <el-tag type="success" size="big" style="width:125px;height:40px;font-size:16px; margin-left:20px">人机并行计算</el-tag>
                      <el-tag type="info" size="big" style="width:125px;height:40px;font-size:18px; margin-left:5px">人机计算状态</el-tag>
              <el-progress type="circle" :percentage="25" style="margin-left:20px"></el-progress>
              <div class="computing">
                  <span style="display:block">计算中</span>
                  <img :src="url.url" style="height: 80px;width:80px"></img>
                  </div>
              <el-progress type="circle" :percentage="50" style="margin-left:10px"></el-progress>
              <div class="computing">
                 <span style="display:block">计算中</span>
                  <img :src="url1.url1" style="height: 80px;width:80px"></img>
                  </div>
                </el-card>
            </el-col>
            <el-col :span="12">
                <el-card shadow="hover" style="height: 285px" >
                       <div class="content-title" style="margin-bottom:30px">策略选择</div>
    <el-tag type="info" size="big" style="width:132px;height:40px;font-size:18px; margin-left:50px">当前分配策略:</el-tag>
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
                      </div>
                </el-card>
            </el-col>
        </el-row>
        <!-- <div class="plugins-tips">
                vue-schart：vue.js封装sChart.js的图表组件。
                访问地址：
                <a
                    href="https://github.com/lin-xin/vue-schart"
                    target="_blank"
                >vue-schart</a>
            </div> -->
        <!-- <div class="schart-box">
                <div class="content-title">柱状图</div>
                <schart class="schart" canvasId="bar" :options="options1"></schart>
            </div> -->
        <!--  <div class="schart-box">
                <div class="content-title">饼状图</div>
                <schart class="schart" canvasId="pie" :options="options3"></schart>
            </div> -->
    </div>
</template>

<script>
import Schart from 'vue-schart';
export default {
    name: 'basecharts',
    components: {
        Schart
    },
    data() {
        return {
            url: { url: require('../../assets/img/human.gif') },
             url1: { url1: require('../../assets/img/computer.gif') },
            options2: {
                tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b}: {c} ({d}%)'
                },
                series: [
                    {
                        name: '访问来源',
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
                            { value: 335, name: '已完成'},
                            { value: 700, name: '未完成' },
                        ]
                    },
                    {
                        name: '详细数据',
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
                                    fontSize: 16,
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
                            { value: 235, name: '机器完成' },
                            { value: 100, name: '人工完成' },
                            { value: 350, name: '机器未完成' },
                            { value: 350, name: '人工未完成' },
                        ]
                    }
                ]
            }
        };
    },
    methods: {
        getMap() {
            var myChart = this.$echarts.init(document.getElementById('map'));
            let option = {
                xAxis: {
                    type: 'category',
                    // data: this.dataX,
                    data: ['第1次迭代', '第2次迭代', '第3次迭代', '第4次迭代', '第5次迭代'],
                    boundaryGap: false, //控制日期是否在中间显示
                    axisLabel: {
                        show: true, //是否显示日期
                        interval: 0, //强制显示全部 // rotate: 40,//倾斜的角度
                        textStyle: {
                            color: '#000', //日期的颜色
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
                            color: '#000' //数字的颜色
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
                        data: [50, 70, 80, 85, 95],
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
    mounted: function () {
        this.getMap();
           var myChart = this.$echarts.init(document.getElementById('map2'));
           myChart.setOption(this.options2);
    }
};
</script>

<style scoped>
.schart-box {
    display: inline-block;
    margin: 10px;
}
.schart {
    width: 600px;
    height: 250px;
}
.content-title {
    clear: both;
    font-weight: 400;
    line-height: 20px;
    font-size: 20px;
    color: #1f2f3d;
}
.computing{
  display :inline-block;
  text-align: center;
  font-size:22px;
  color: red;
  font-weight:500;
}
.description{
      margin-right:20px;
      font-size:18px;
      color:grey;
      font-weight:600;

}
.description-box{
    margin-top:20px;
}
</style>