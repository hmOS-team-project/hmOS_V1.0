<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-lx-people"></i> 人机计算接口</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <el-row :gutter="20">
         <el-col :span="14">
         <el-card shadow="hover" style="height:580px;">
             <div slot="header" class="clearfix">
                   <i class="el-icon-picture grid-con-icon1"></i>
                   <span>待处理视频帧</span>
            </div>
                        <div class="container-box2">
                    <div class="container-box2-header">
                     待处理
                    </div>
                    <img src="../../assets/img/person1.png"  alt="" class="container1-box2-img"/>
                     <img src="../../assets/img/person2.png"  alt="" class="container1-box2-img"/>
                       <img src="../../assets/img/person3.png"  alt="" class="container1-box2-img"/>
                        <img src="../../assets/img/person4.png"  alt="" class="container1-box2-img"/>
                </div>
            <div class="container-box1">
                    <div class="container-box1-header">
                     已完成
                    </div>
                   <img src="../../assets/img/person1.png"  alt="" class="container1-box1-img"/>
                     <img src="../../assets/img/person2.png"  alt="" class="container1-box1-img"/>
                       <img src="../../assets/img/person3.png"  alt="" class="container1-box1-img"/>
                        <img src="../../assets/img/person4.png"  alt="" class="container1-box1-img"/>
                </div>
            <div class="grid-content grid-con-1">
                <i class="el-icon-lx-camera grid-con-icon"></i>
                   <div class="grid-cont-right">
                      <div class="grid-num">100/150</div>
                      <div>待处理/已完成</div>
                    </div>
             </div>
         </el-card>
            </el-col>
            <el-col :span="10">
         <el-card shadow="hover" style="height:580px;">
            <div slot="header" class="clearfix">
                 <i class="el-icon-lx-people grid-con-icon1"></i>
                  <span>操作反馈区</span>
            </div>
            <img :src="url.url" style="height: 230px;width:250px"></img>
            <div class="work-time">
                    <span>工作时长</span>
                    <span class="start-time">开始时间：{{ start_time }}</span>
                    <span class="start-time">用时：{{ count_time }}</span>
            </div>
                <img src="../../assets/img/person1.png"  alt="" class="crop-img"/>
                <el-button type="primary" style="margin:50px 20px 0 15px;height:50px;width:100px">True</el-button>
                    <el-button type="primary" style="margin:30px 20px 0 0;height:50px;width:100px">False</el-button>
                  <el-button type="primary" style="margin:30px 20px 0 15px;height:50px;width:100px">撤销</el-button>
                    <el-button type="primary" style="margin:30px 20px 0 0;height:50px;width:100px">保存</el-button>
          </el-card>
            </el-col>
        </el-row>
        <!-- <div class="container">
            <div class="plugins-tips">
                Vue-Quill-Editor：基于Quill、适用于Vue2的富文本编辑器。
                访问地址：<a href="https://github.com/surmon-china/vue-quill-editor" target="_blank">vue-quill-editor</a>
            </div>
            <quill-editor ref="myTextEditor" v-model="content" :options="editorOption"></quill-editor>
            <el-button class="editor-btn" type="primary" @click="submit">提交</el-button>
        </div> -->

        <!-- <div class="container1">
            <div class="container1-box1">
                <div class="container1-box11">
                    <div class="container1-box1-img1">
                        <img src="../../assets/img/str1.png"  alt="" class="container1-box1-img"/>
                        <img src="../../assets/img/str2.png"  alt="" class="container1-box1-img"/>
                        <img src="../../assets/img/str3.png"  alt="" class="container1-box1-img"/>
                        <img src="../../assets/img/str4.png"  alt="" class="container1-box1-img"/>
                        <img src="../../assets/img/str5.png"  alt="" class="container1-box1-img"/>
                        <img src="../../assets/img/str6.png"  alt="" class="container1-box1-img"/>
                        <img src="../../assets/img/str7.png"  alt="" class="container1-box1-img"/>
                        <img src="../../assets/img/str8.png"  alt="" class="container1-box1-img"/>
                        <img src="../../assets/img/str9.png"  alt="" class="container1-box1-img"/>
                        <img src="../../assets/img/str10.png"  alt="" class="container1-box1-img"/>
                    </div>
                </div>
            </div>
            <div class="container1-box2">
                <div class="container1-box21">
                    <img src="../../assets/img/str1.png"  alt="" class="container1-box2-img"/>
                </div>
                <div class="container1-box22">
                    <button class="container1-btn3" type="submit">True</button>
                    <button class="container1-btn4" type="submit">False</button>
                </div>
            </div>
        </div> -->
    </div>
</template>

<script>
import 'quill/dist/quill.core.css';
import 'quill/dist/quill.snow.css';
import 'quill/dist/quill.bubble.css';
import { quillEditor } from 'vue-quill-editor';
export default {
    name: 'editor',
    data: function () {
        return {
            url: { url: require('../../assets/img/work.gif') },
            start_time: (new Date()).getFullYear()+'-'+((new Date()).getMonth()+1)+'-'+(new Date()).getDate()+' '+(new Date()).getHours()
            +':'+(new Date()).getMinutes()+':'+(new Date()).getSeconds(),
            count_time: '00:00:00',
            content: '',
            editorOption: {
                placeholder: 'Hello World'
            }
        };
    },
    components: {
        quillEditor
    },
    methods: {
        onEditorChange({ editor, html, text }) {
            this.content = html;
        },
        submit() {
            console.log(this.content);
            this.$message.success('提交成功！');
        },
        countTime(startTime) {
            if (!startTime) return;
            let start_time = new Date(startTime);
            let _this = this;
            this.timer = setInterval(() => {
                let millisecond = new Date() - start_time;
                let h = Math.floor(millisecond / (60 * 60 * 1000));
                h = h < 10 ? '0' + h : h;
                let min = Math.floor((millisecond % (60 * 60 * 1000)) / (60 * 1000));
                min = min < 10 ? '0' + min : min;
                let sec = Math.floor(((millisecond % (60 * 60 * 1000)) % (60 * 1000)) / 1000);
                sec = sec < 10 ? '0' + sec : sec;
                _this.count_time = h + ':' + min + ':' + sec;
            }, 1000);
        }
    },

    created() {
        // 调用时机根据需求
        this.countTime(this.start_time);
    },
    beforeDestroy() {
        if (this.timer) {
            clearInterval(this.timer);
        }
    }
};
</script>
<style scoped>
/* .editor-btn{
        margin-top: 20px;
    } */

.container-box1 {
    display: inline-block;
    vertical-align: top;
    width: 300px;
    height: 400px;
    margin-left: 20px;
    border-radius: 10%;
    /* background-color: black; */
    border: 3px dashed #c0c0c0;
}
.container-box1-header {
    height: 50px;
    font-size: 24px;
    color: rgb(100, 213, 114);
    text-align: center;
}
.container-box2 {
    vertical-align: top;
    display: inline-block;
    width: 320px;
 height: 400px;
    margin-left: 20px;
    border-radius: 10%;
    /* background-color: black; */
    border: 3px dashed #c0c0c0;
}
.container-box2-header {
    height: 50px;
    font-size: 24px;
    color: rgb(242, 94, 67);
    text-align: center;
}
.container1-box1-img {
    display: inline-flex;
    width: 120px;
    height: 150px;
    margin-left: 16px;
    margin-top: 5px;
}
.container1-box2-img {
    display: inline-flex;
    width: 120px;
    height: 150px;
    margin-left: 24px;
    margin-top: 5px;
}
.container1-btn3 {
    width: 50px;
    height: 40px;
    margin-top: 5px;
    margin-left: 80px;
    background-color: #409eff;
    color: white;
}
.container1-btn4 {
    width: 50px;
    height: 40px;
    margin-left: 50px;
    background-color: #409eff;
    color: white;
}
.grid-content {
    padding: 20px 0px;
    height: 80px;
}

.grid-cont-right {
    vertical-align: middle;
    width: 120px;
    display: inline-block;
    text-align: center;
    font-size: 14px;
    color: #999;
}

.grid-num {
    font-size: 24px;
    font-weight: bold;
}

.grid-con-icon {
    vertical-align: middle;
    display: inline-block;
    margin-left: 300px;
    font-size: 24px;
    width: 40px;
    height: 40px;
    text-align: center;
    line-height: 40px;
    color: #fff;
}
.grid-con-icon1 {
    vertical-align: middle;
    display: inline-block;
    font-size: 24px;
    width: 40px;
    height: 40px;
    text-align: center;
    line-height: 40px;
    color: black;
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
.work-time {
    width: 200px;
    margin-top: 30px;
    vertical-align: top;
    display: inline-block;
    text-align: center;
    font-size: 28px;
    font-weight: 600;
    color: rgb(242, 94, 67);
}
.start-time{
    margin-top:15px;
    display:block;
     width: 220px;
     font-size: 20px;
}
.crop-img{
    float:left;
    margin-top:30px;
    margin-left:60px;
    width: 150px;
    height: 200px;
}
</style>