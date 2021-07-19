<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-lx-home"></i> 任务类型</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <el-row :gutter="18">
            <el-col :span="15">
                <el-card shadow="hover" style="height: 580px" :body-style="{ padding: '0px' }">
                        <div class="header-box1">
                        <img src="../../assets/img/icon-typeselect.png" style="width: 45px; height: 45px" />
                        <span style="color:white;font-size:20px">类型选择</span>
                        </div>
                    <div style="display: flex; flex-wrap: wrap">
                        <div class="tasktype1">
                            <div class="tasktype1-box">
                                <img src="../../assets/img/icon-type1.png" style="width: 80px; height: 80px" />
                                <div class="tasktype-name">分类任务</div>
                            </div>
                        </div>
                        <div class="tasktype2">
                            <div class="tasktype2-box" @click="taskinput()">
                                <img src="../../assets/img/icon-type2.png" style="width: 80px; height: 80px" />
                                <div class="tasktype-name">识别任务</div>
                            </div>
                        </div>
                        <div class="tasktype3">
                            <div class="tasktype3-box">
                                <img src="../../assets/img/icon-type3.png" style="width: 80px; height: 80px" />
                                <div class="tasktype-name">生成任务</div>
                            </div>
                        </div>
                        <div class="tasktype4">
                            <div class="tasktype4-box">
                                <img src="../../assets/img/icon-type4.png" style="width: 80px; height: 80px" />
                                <div class="tasktype-name">其他任务</div>
                            </div>
                        </div>
                    </div>
                </el-card>
            </el-col>
            <el-col :span="9">
                <el-card shadow="hover" style="height: 580px" :body-style="{ padding: '0px' }">
                    <div class="header-box2">
                        <img src="../../assets/img/icon-typeinformation.png" style="width: 45px; height: 45px" />
                        <span style="color:white;font-size:20px">类型划分</span>
                        </div>
                    <div class="typeinformation-cont">
                        <div class="typeinformation-box">
                            <div class="typeinformation-header">
                                <img src="../../assets/img/icon-type1.png" style="width: 30px; height: 30px" />
                                <span class="typeinformation-title">分类任务</span>
                            </div>
                            <div class="typeinformation-name-box">
                                <div class="typeinformation-name1">
                                    多类别分类
                                </div>
                                  <div class="typeinformation-name1">
                                    多标签分类
                                </div>
                              <div class="typeinformation-name1">
                                   不平衡分类
                                </div>
                            </div>
                        </div>
                                            <div class="typeinformation-box">
                            <div class="typeinformation-header">
                                <img src="../../assets/img/icon-type2.png" style="width: 30px; height: 30px" />
                                <span class="typeinformation-title">识别任务</span>
                            </div>
                            <div class="typeinformation-name-box">
                                <div class="typeinformation-name2">
                                   文本识别
                                </div>
                                  <div class="typeinformation-name2">
                                    图像识别
                                </div>
                              <div class="typeinformation-name2">
                                   声音识别
                                </div>
                            </div>
                        </div>
                                            <div class="typeinformation-box">
                            <div class="typeinformation-header">
                                <img src="../../assets/img/icon-type3.png" style="width: 30px; height: 30px" />
                                <span class="typeinformation-title">生成任务</span>
                            </div>
                            <div class="typeinformation-name-box">
                                <div class="typeinformation-name3">
                                    图像生成
                                </div>
                                  <div class="typeinformation-name3">
                                    语音生成
                                </div>
                            </div>
                        </div>
                                            <div class="typeinformation-box">
                            <div class="typeinformation-header">
                                <img src="../../assets/img/icon-type4.png" style="width: 30px; height: 30px" />
                                <span class="typeinformation-title">其他任务</span>
                            </div>
                            <div class="typeinformation-name-box">
                                <div class="typeinformation-name4">
                                    文本翻译
                                </div>
                            </div>
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
        taskinput(){
               this.$router.push('/identificationtask');
        },
    },
};
</script>


<style scoped>
.grid-content {
    display: flex;
    align-items: center;
    height: 40px;
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
.tasktype1 {
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    background: radial-gradient(rgba(185, 171, 171, 0), #FFB5C5);
    text-align: center;
    height: 230px;
    width: 360px;
    margin: 10px;
}
.tasktype2 {
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    background: radial-gradient(rgba(185, 171, 171, 0), #aeeeee);
    text-align: center;
    height: 230px;
    width: 360px;
    margin: 10px;
}
.tasktype3 {
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    background: radial-gradient(rgba(185, 171, 171, 0), #9aff9a);
    text-align: center;
    height: 230px;
    width: 360px;
    margin: 10px;
}
.tasktype4 {
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    background: radial-gradient(rgba(185, 171, 171, 0), #bebebe);
    text-align: center;
    height: 230px;
    width: 360px;
    margin: 10px;
}
.tasktype-name {
    font-size: 22px;
    font-weight: 800;
}
.typeinformation-title{
    font-size:22px;
    font-weight: 800;
    margin-left:10px;
}
.typeinformation-header{
    display: flex;
    align-items: center;
}
.typeinformation-name-box{
    display: flex;
    align-items: center;
}
.typeinformation-name1{
    text-align: center;
    width:95px;
    margin: 25px 15px 25px 15px;
    background-color:#FFB5C5;
    font-size:18px;
    cursor: pointer;
}
.typeinformation-name2{
    text-align: center;
    width:95px;
    margin: 25px 15px 25px 15px;
    background-color:#aeeeee;
    font-size:18px;
        cursor: pointer;
}
.typeinformation-name3{
    text-align: center;
    width:95px;
    margin: 25px 15px 25px 15px;
    background-color:#9aff9a;
    font-size:18px;
        cursor: pointer;
}
.typeinformation-name4{
    text-align: center;
    width:95px;
    margin: 25px 15px 25px 15px;
    background-color:#bebebe;
    font-size:18px;
        cursor: pointer;
}
.header-box1{
    width:200px;
    height:50px;
    background: url('../../assets/img/icon-typebackground.png') no-repeat;
    background-size: 100% 100%;
        display: flex;
    align-items: center;
}
.header-box2{
    width:200px;
    height:50px;
    background: url('../../assets/img/icon-typebackground.png') no-repeat;
    background-size: 100% 100%;
        display: flex;
    align-items: center;
}
.typeinformation-cont{
    padding:15px;
}
</style>
