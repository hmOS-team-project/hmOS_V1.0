
<template>
    <div>
        <div>
        <div id="loading" style="display: none">
            
        </div>
        <div class="Hometitlebox">
       <img src="../../assets/img/logo2.png"   style="width:50px;height:50px;margin-right:25px"/>
            <a style="color: #00e4ff">hmOS1.0</a>
             <img src="../../assets/img/logo1.png" style="width:60px;height:50px;margin-left:15px"/>
            </div>
        <div class="navigation">
            <ul >
        　　<li class="l1" title="system settings" ></li>
        　　<li class="l2" title="backup"></li>
        　　<li class="l3" title="log"></li> 
        　　<li class="l4" title="repairing"></li>
            <li class="l5" title="information"></li>   
        　　</ul>
        </div>
                 <!--侧边浮窗-->
       <div class="rect1" style="margin-left:50px;height:550px;background-color: rgba(11, 2, 37, 0.7);" >
                <span class="analyzedatashowtitle" style="line-height: 66px;">【System information】</span>
                <div class="scrollbox">
                    <div id="scrollDiv" >
                        <ul style="margin-top: -1.48947px;">
                            <li>Space usage <span >280M</span></li>
                            <li>Database usage  <span >4G</span></li>
                            <li>Creation time <span >2021/6/30</span></li>
                            <li>Task number <span >four</span></li>
                        </ul>
                    </div>
                </div>
       </div>
        <div class="grid" >
            <!--左上分析内容放置框-->
        <div  class="horn"> 
            <div class="title">
                Visitors
            </div>
            
            <div id="charts" style="width:340px; height:200px"></div>   
            
               
        </div>
            <!--右上分析内容放置框-->
        <div class="horn" style="margin-left:10px;" > 
        <div class="title">
              Task monitor
            </div> 
        <div class="maintainer_info" >
            <ul style="height:220px">
        <li >
            <div class="com" >
                Task
            </div>
        </li>
        <li>
            <div class="com" >
                Priority
            </div>
        </li>
        <li>
            <div class="com" >
                Status
            </div>
        </li>
        <li>
            <div class="name">
               OCR
            </div>
        </li>
        <li>
            <div  class="high" >
                high
            </div>
        </li>
        <li>
            <div class="running" >
                running
            </div>
        </li>
        <li>
            <div class="name">
                SED
            </div>
        </li>
        <li>
            <div  class="low" >
               low
            </div>
        </li>
        <li>
            <div class="error" >
                error
            </div>
        </li>
        <li>
            <div class="name">
                ASR
            </div>
        </li>
        <li>
            <div  class="middle" >
               middle
            </div>
        </li>
        <li>
            <div class="exception" >
                exception
            </div>
        </li>
    </ul>
        </div>
        <div>
            </div> 
            
        </div>    
       <!--左下分析内容放置框-->
        <div class="horn"> 
        <div class="title">
          Task execution status
        </div>
        <div id="circle" style="width:340px;height:300px;margin-top:0">

        </div>
        </div> 
         <!--右下分析内容放置框-->
        <div class="horn" style="margin-left:10px;"> 
            <div class="title">
              Maintainer
              </div>
              <div class="maintainer_info" >
            <ul style="height:220px">
            <li >
                <div class="com" >
                    Shift
                </div>
            </li>
            <li>
                <div class="com" >
                    Staff
                </div>
            </li>
            <li>
                <div class="com">
                    Telephone
                </div>
            </li>
             <li >
                <div class="name" >
                  <img src="../../assets/img/sun.png"   style="width:20px;height:20px;margin-bottom:5px;margin-right:5px"/>
                   <span >day</span>
                </div>
            </li>
            <li>
                <div class="name" >
                    gst
                </div>
            </li>
            <li>
                <div class="name">
                    15991983787
                </div>
                <li >
                <div class="name" >
                   <img src="../../assets/img/sun.png"   style="width:20px;height:20px;margin-bottom:5px;margin-right:5px"/>
                   <span >day</span>
                </div>
            </li>
            <li>
                <div class="name" >
                    lps
                </div>
            </li>
            <li>
                <div class="name">
                    18637096781
                </div>
            </li>
             <li >
                <div class="com" >
                    Shift
                </div>
            </li>
            <li>
                <div class="com" >
                    Staff
                </div>
            </li>
            <li>
                <div class="com">
                    Telephone
                </div>
            </li>
             <li >
                <div class="name" >
                  <img src="../../assets/img/moon.png"   style="width:20px;height:20px;margin-bottom:5px;margin-right:5px"/>
                   <span >night</span>
                </div>
            </li>
            <li>
                <div class="name" >
                    lyw
                </div>
            </li>
            <li>
                <div class="name">
                    15991983787
                </div>
                <li >
                <div class="name" >
                   <img src="../../assets/img/moon.png"   style="width:20px;height:20px;margin-bottom:5px;margin-right:5px"/>
                   <span >night</span>
                </div>
            </li>
            <li>
                <div class="name" >
                    kyh
                </div>
            </li>
            <li>
                <div class="name">
                    18637096781
                </div>
            </li>
            </ul>
            
        </div>
        </div> 
        </div>
        
        
         <div  class="navigation" style="float:right;" >
        <ul >
        　　<li class="l1" title="system settings" ></li>
        　　<li class="l2" title="backup"></li>
        　　<li class="l3" title="log"></li> 
        　　<li class="l4" title="repairing"></li>
            <li class="l5" title="information"></li>   
　　</ul>
        </div>
        <div style="height:550px;width:250px;float:right;margin-right:30px;margin-left:30px;">
        <div class="rect1" style="height:50%;background-color: rgba(11, 2, 37, 0.7);">
            <el-row>

              <el-col :span="16"><span class="analyzedatashowtitle" style="line-height: 66px;">【GPU Unit】</span></el-col>
              <el-col :span="8">
                  <el-row>
                   <el-col :span="12"> <div class="temperature"></div></el-col>
                  <el-col  :span="12"><div class="degree" >36℃</div></el-col>
                  </el-row>
                  
            </el-col>
             </el-row>
            
                
        <div style="height:100%;width:250px;margin-right:20px">
            <div style="height:100%;width:250px">
                <div class="gpu" >
                    <div style="width:50px;float:left;" >gpu1</div>
                    <div class="progress"  >
                        <div class="progress-bar">
                        <div class="progress-value">80%</div>
                    </div>
                    </div>
                </div>
                <div class="gpu">
                     <div style="width:50px;float:left;" >gpu2</div>
                    <div class="progress"  >
                        <div class="progress-bar" style="width:60%">
                        <div class="progress-value">60%</div>
                    </div>
                     </div>
                </div>
                <div class="gpu">
                    <div style="width:50px;float:left;" >gpu3</div>
                    <div class="progress"  >
                        <div class="progress-bar" style="width:30%">
                        <div class="progress-value">30%</div>
                    </div>
                    </div>
                </div>
                <div class="gpu" >
                    <div style="width:50px;float:left;" >gpu4</div>
                    <div class="progress"  >
                        <div class="progress-bar" style="width:50%">
                        <div class="progress-value">50%</div>
                    </div>
                    </div>
                </div>
                <div class="gpu" >
                    <div style="width:50px;float:left;" >gpu5</div>
                    <div class="progress"  >
                        <div class="progress-bar" style="width:70%">
                        <div class="progress-value">70%</div>
                    </div>
                    </div>
                </div>
                <div class="gpu" >
                    <div style="width:50px;float:left;" >gpu6</div>
                    <div class="progress"  >
                        <div class="progress-bar" style="width:40%">
                        <div class="progress-value">40%</div>
                    </div>
                    </div>
                </div>
                <div class="gpu" >
                    <div style="width:50px;float:left;" >gpu7</div>
                    <div class="progress"  >
                        <div class="progress-bar" style="width:65%">
                        <div class="progress-value">65%</div>
                    </div>
                    </div>
                </div>
                <div class="gpu" >
                    <div style="width:50px;float:left;" >gpu8</div>
                    <div class="progress"  >
                        <div class="progress-bar" style="width:55%">
                        <div class="progress-value">55%</div>
                    </div>
                    </div>
                </div>

                </div>
                 
               
                
               
            
            
        </div>
        
        </div>
        <div class="rect1" style="height:46%;margin-top:20px;background-color: rgba(11, 2, 37, 0.7);">
            
          <el-row >

              <el-col :span="16"><span class="analyzedatashowtitle" style="line-height: 66px;">【CPU Unit】</span></el-col>
              <el-col :span="8" style="line-height: 30px;">
                  <el-row>
                   <el-col :span="12"> <div class="temperature"></div></el-col>
                  <el-col  :span="12"><div class="degree" >36℃</div></el-col>
                  </el-row>
                  
            </el-col>
             </el-row>
             <div id="echartsBar" style="width:220px;height: 150px;"> </div>
        
                </div>
                
        </div>
    </div>
     
        <div class="copyrigntoutbox" style="position: fixed;  bottom:33px ;">
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
import echarts from 'echarts';

// 引入饼状图组件
require('echarts/lib/chart/pie')
// 引入提示框和title组件
require('echarts/lib/component/tooltip')
require('echarts/lib/component/title')


export default {
     data() {
         return{
             percentage:20,
             color:'rgb(0, 168, 255)',
            
         }
     },
    mounted() {
         this.drawLine();
         this.drawcicle();
         this.echartsBarInit();
       
         window.onload = function () {
            var loading = document.getElementById('loading');
            loading.style.display = 'none';
        };
        $('#scrollDiv').Scroll({
            line: 1,
            speed: 500,
            timer: 5000,
            up: 'but_up',
            down: 'but_down',
        })
       
    },
    methods:{
       
        echartsBarInit()
        {
            let myChart = echarts.init(document.getElementById('echartsBar'));
        myChart.setOption({
            
          
            grid: {
                    containLabel: true,
                    left: 0,
                    right:'5px',
                    top:'15px',
                    bottom:'5px',
                },
                xAxis: {
                    type: 'category',
                    splitLine: {
                        show: false
                    }, //坐标轴在 grid 区域中的分隔线
                    
                    axisTick: {
                        show: true
                    }, //坐标轴刻度
                    axisLine: {
                        lineStyle:{
                            color:'white',
                        },
                        show: true
                    }, //坐标轴轴线
                     axisLabel: {
                        show: true,
                        color: 'white',
                        fontSize: 12
                    },//坐标轴刻度标签
                    data: ['cpu1','cpu2','cpu3','cpu4']
                },
                yAxis: {
                    splitLine:{
                        lineStyle:{
                            color:'rgba(0, 168, 255 ,0.2)',
                        },
                         
                    },
                    type: 'value',
                    axisTick: {
                        show: true
                    },
                    axisLine: {
                        lineStyle:{
                            color:'white',
                        },
                        show: true
                    },
                    
                    axisLabel: {
                        formatter:'{value} %',

                        show: true,
                        color: 'white',
                        fontSize: 12
                    },//坐标轴刻度标签
                    data: ['20','40','60','80','100']
                },
                series: [{
                    color:'white',
                    type: "bar",
                    barWidth: 8,
                     zlevel:1,
                    
                    
                    itemStyle: {
                        normal: {
                            barBorderRadius: 4,
                            color: new echarts.graphic.LinearGradient(1, 0, 0, 0, [{
                                offset: 0,
                                color: 'rgba(75, 197, 253, 0)'
                            },
                                {
                                    offset: 1,
                                    color: 'rgba(168, 197, 253, 1)'
                                }
                            ])
                        }
                    },

                }, {
                    type: "bar",
                    barGap: '-100%',
                    barWidth: 8,
                    data: [20,40,60,80,100],
                    itemStyle: {
                        normal: {
                            barBorderRadius:4,
                            color: new echarts.graphic.LinearGradient(
                                1, 1, 0, 0, [{
                                    offset: 0,
                                    color: 'rgba(0, 168, 255 ,0.3)'
                                },
                                {
                                    offset: 1,
                                    color:'rgba(0, 168, 255 ,0.8)'
                                }
                            ]
                            ),
                           
                        }
                    },

                }
                ],
                });

        },
         drawcicle()
      {
        let myChart = echarts.init(document.getElementById('circle'))
        myChart.setOption({
          
          tooltip : {
              trigger: 'item',
              formatter: "{a} <br/>{b} : {c} ({d}%)"
          },
          legend: {
              orient: 'vertical',
              bottom: 'right',
              right: 'right',
              data: ['running','邮件营销','联盟广告','视频广告','搜索引擎']
          },
          series : [
              {
                 name:'status',
                  type: 'pie',
                  radius : '55%',
                  center: ['50%', '35%'],
                  data:[
                      {value:335, name:'error'},
                      {value:442, name:'stopping'},
                      {value:234, name:'crash'},
                      {value:135, name:'exception'},
                      {value:1548, name:'running'}
                  ],
                  itemStyle: {
                      emphasis: {
                          shadowBlur: 0,
                          shadowOffsetX: 0,
                          shadowColor: 'rgba(0, 0, 0, 1)'
                      }
                  }
              }
          ]
      });
         },
        drawLine(){
        // 基于准备好的dom，初始化echarts实例
        let myChart = echarts.init(document.getElementById('charts'))
        // 绘制图表
        myChart.setOption({
            tooltip: {},
            
            //铺满
            grid:{
                      top:"20px",
                      
                     
                      bottom:"20px"
                  },
             legend:{
            data:['visitors'],
            
           },
        //x轴
            xAxis:{
                axisLabel: {
                textStyle: {
                color: '#fff'
                    }
                }  ,
                axisLine: {
                lineStyle: {
                color: '#fff', // 颜色    
                }
             } ,
                data:["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
            },
            //y轴没有显式设置，根据值自动生成y轴
            yAxis:{
                axisLabel: {
                textStyle: {
                color: '#fff'
                    }
                }  ,
                axisLine: {
                lineStyle: {
                color: '#fff', // 颜色    
                }},
                splitLine: { 
                    lineStyle:
                    {
                    color:['rgba(0, 168, 255, 0.2)'],
                    },
                },
            },
            
            series:[{
                name:'销量',
                type:'line',
                symbol:'circle',
                symbolSize:6,//折点大小
                 itemStyle : {
                   normal : {
                    color:'rgba(255, 246, 143,1)',//折点颜色
                    lineStyle:{
                                width:2,
                                type:'solid',  //'dotted'虚线 'solid'实线
                                color:'rgba(0, 168, 255 ,0.5)',
                            }

                 }
                },
                
                
                data:[40,20,35,60,55,30,25],
                areaStyle:{   //折线下面区域块的样式
                
                    color:{     //渐变  属性值 同CSS
                    type:"linear",
                    x: 0,
                    y: 0,
                    x2: 0,
                    y2: 1,
                    colorStops: [{
                        offset: 0, color: 'rgba(0, 168, 255, 0.2)' // 0% 处的颜色
                    }, {
                        offset: 1, color: 'rgba(0, 0, 255, 0.8)' // 100% 处的颜色
                    }],
                },
                

               }
            }]
            
        });
        }
    }
}
</script>
<style scoped>


/* 渐变进度条 */
.progress-value{
    height: 10px;
}
.progress {
	position: relative;
	width: 180px;
	height: 10px;
	background:rgba(0, 168, 255, 0.2);
	border-radius: 10px;
    margin-top: 3px;
}
.progress-bar {
   
	position: absolute;
	left: 0;
	
	width: 80%;
	
	line-height: 10px;
	border-radius: 10px;
	background: linear-gradient(to right, #da81a1 35%, #7aa4c8 68%);
	font-size: 12px;
	color: #fff;
	text-align: center;
	-webkit-transition: 80% .6s ease;
	-o-transition: 80% .6s ease;
	transition: 80% .6s ease;
	animation: animate-positive 2s;
}

@-webkit-keyframes animate-positive{
	0% { width: 0%; }
}
@keyframes animate-positive{
	0% { width: 0%; }
}

.gpu{
    height:20px;
    width:250px;
    font-size: 12px;
}
.degree{
    margin-left:5px;
    margin-top:20px;
    font-weight: bold;
    color: cyan;
}
.temperature{
    height:64px;
    background:url(../../assets/img/temperature.png) ;
    background-repeat:no-repeat; 
    background-size:100% 50%;
    -moz-background-size:100% 100%;
    background-position: center;
}
.gpu_usage{
    width:16%;
   height: 550px;
     float: left;
}
.title{
width:100%;
height:30px;
text-align:center;
font-weight:bold;
}

.day{
    width:20px;
    background:url(../../assets/img/sun.png) ;
    background-repeat:no-repeat; 
    background-size:100% 100%;
    -moz-background-size:100% 100%;
    background-position: center;
}
.high{
    opacity:0.7;
    background-image: url(../../assets/img/red.png);
    background-repeat:no-repeat; 
    background-size:70% 100%;
    -moz-background-size:100% 100%;
    background-position: center;
}
.middle{
    opacity:0.7;
    background-image: url(../../assets/img/orange.png);
    background-repeat:no-repeat; 
    background-size:70% 100%;
    -moz-background-size:100% 100%;
    background-position: center;
}
.low{
    opacity:0.7;
    background-image: url(../../assets/img/blue.png);
    background-repeat:no-repeat; 
    background-size:70% 100%;
    -moz-background-size:100% 100%;
    background-position: center;
}
li {
list-style:none;
}
.maintainer_info{
    width:340px;
    height:200px;
    text-align:center;
    font-weight:lighter;
    font-size:14px;
}
.maintainer_info ul {
  overflow: hidden;
  width:340px;
  margin-left: -20px;
  margin-right:10px;
  
}
.maintainer_info ul li {
  width:33.3%;
  height: 30px;
  float: left;
 text-align:center;
  box-sizing: border-box;

  
}
.maintainer_info ul li .com {
  color:rgb(0, 217, 255);
  height: inherit;
  font-weight:450;
}
.grid{
    position: absolute;
    width:600px;
    height:550px;
   margin: 20px;
    margin-top:35px;
    margin-left: 10px;
    display: grid;
    grid-template: repeat(2, 1fr) / repeat(2, 1fr);
    top: 50%; 
    left: 50%; 
    transform: translate(-58%,0); 
}
div {
    color:#FFFFFF;
   
}
.charts{
    height:200px;
    width: 200px;
    position: absolute;
}
.navigation{
    margin-top:50px;
    float:left;
    box-shadow: 0px 0px 15px #837979;
    width:5%;
    height:550px;
    background-color: rgba(11, 2, 37, 0.6);
    
}
.l1{
height:80px;
margin-top: 10px;
background-image: url(../../assets/img/setting1.png);
background-repeat:no-repeat; 
background-size:100% 100%;
-moz-background-size:100% 100%;
}
.l2{
height:80px;
margin-top: 20px;
background-image:url(../../assets/img/Upload.png);
background-repeat:no-repeat; 
background-size:90% 90%;
-moz-background-size:100% 100%;
}

.l3{
height:80px;
margin-top: 10px;
background-image: url(../../assets/img/log1.png);
background-repeat:no-repeat; 
background-size:90% 90%;
-moz-background-size:100% 100%;
}
.l4{
height:80px;
margin-top: 20px;
background-image:url(../../assets/img/repair.png);
background-repeat:no-repeat; 
background-size:100% 100%;
-moz-background-size:100% 100%;
}
.l5{
height:80px;
margin-top: 20px;
background-image:url(../../assets/img/info.png);
background-repeat:no-repeat; 
background-size:100% 100%;
-moz-background-size:100% 100%;

}
.l1:hover{
     background-color:  rgba(2, 22, 59, 0.5);   
}
.l2:hover{
     background-color: rgba(29, 69, 141, 0.5);  
}
.l3:hover{
     background-color: rgba(2, 22, 59, 0.5);   
}
.l4:hover{
     background-color:  rgba(2, 22, 59, 0.5); 
}
.l5:hover{
     background-color:  rgba(2, 22, 59, 0.5); 
}
.rect1 {
    float:left;
    box-shadow: 0 0 15px #2b44cf;
    margin-top: 50px;
    padding:10px;
    width: 250px;
    overflow: hidden;
    
    background: linear-gradient(to left, #00faff, #00faff) left top no-repeat, 
                linear-gradient(to bottom, #00faff, #00faff) left top no-repeat, 
                linear-gradient(to left, #00faff, #00faff) right top no-repeat,
                linear-gradient(to bottom, #00faff, #00faff) right top no-repeat, 
                linear-gradient(to left, #00faff, #00faff) left bottom no-repeat,
                linear-gradient(to bottom, #00faff, #00faff) left bottom no-repeat,
                linear-gradient(to left, #00faff, #00faff) right bottom no-repeat,
                linear-gradient(to left, #00faff, #00faff) right bottom no-repeat;
    background-size: 4px 20px, 20px 4px, 4px 20px, 20px 4px;  

}
.horn {
   
    margin-top: 50px;
    
    
      box-shadow: 0px 0px 10px #837979;
      float:left;
      padding:10px;
      
      background-color: rgba(11, 2, 37, 0.5);
      width: 340px;
      height: 250px;
   
      border: 2px solid #00d3e7;
   
      border-image: -webkit-linear-gradient(rgb(85, 87, 231), rgb(149, 228, 241)) 20 20;
      border-image: -moz-linear-gradient(rgb(85, 87, 231), rgb(149, 228, 241)) 20 20;
      border-image: -o-linear-gradient(rgb(85, 87, 231), rgb(149, 228, 241)) 20 20;
      border-image: linear-gradient(rgb(85, 87, 231), rgb(149, 228, 241)) 20 20;
    }
.scrollbox {
    width: 250px;
    margin: 0 auto;
}

#scrollDiv {
    width: 2250px;
    height: 280px;
    overflow: hidden;
}

/*这里的高度和超出隐藏是必须的*/
#scrollDiv ul li {
    height: 33px;
    width: 230px;
    margin-right:10px;
    background-color:rgba(0, 153, 255, 0.2);
    overflow: hidden;
    margin-bottom: 6px;
    color: #dfdede;
    font-size: 14px;
    padding: 0 9px 0 9px;
    line-height: 30px;
    position: relative;
    border-color: teal;
}

#scrollDiv ul li span {
    position: absolute;
    bottom: 3px;
    right: 10px;
    display: block;
    width: 68px;
    height: 22px;
    text-align: center;
   
    color:white;
    border-radius: 4px;
    line-height: 18px;
     background-color:rgba(199, 197, 64,0.7)
      
}
</style>