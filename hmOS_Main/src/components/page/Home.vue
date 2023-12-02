<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-lx-home"></i> 系统首页</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <el-row :gutter="18">
            <el-col :span="8">
                <el-card :body-style="{ padding: '0px' }" shadow="hover" style="height: 270px" class="mgb20">
                    <div class="user-info">
                        <img src="../../assets/img/img.jpg" class="user-avator" alt />
                        <div class="user-info-cont">
                            <div class="user-info-name">{{ name }}</div>
                            <div>{{ role }}</div>
                        </div>
                        <div class="information">个人中心</div>
                    </div>
                    <div class="user-func">
                        <div class="user-func-box">
                            <img src="../../assets/img/mytask.png" />
                            <div class="user-func-name">我的任务</div>
                        </div>
                        <div class="divider"></div>
                        <div class="user-func-box">
                            <img src="../../assets/img/mynews.png" />
                            <div class="user-func-name">我的消息</div>
                        </div>
                    </div>
                </el-card>
                <el-card :body-style="{ padding: '0px' }" shadow="hover" style="height: 270px" class="mgb20">
                    <div class="resource-info">
                        <img src="../../assets/img/icon-resource.png" class="user-avator" alt />
                        <div class="resource-info-cont">系统资源</div>
                    </div>
                    <div class="user-func">
                        <div class="user-func-box">
                            <img src="../../assets/img/icon-gpu.png" style="width: 80px; height: 80px" />
                            <div class="user-func-name">80/100</div>
                        </div>
                        <div class="divider"></div>
                        <div class="user-func-box">
                            <img src="../../assets/img/icon-human.png" style="width: 80px; height: 80px" />
                            <div class="user-func-name">4/10</div>
                        </div>
                    </div>
                </el-card>
            </el-col>
            <el-col :span="16">
                <el-card :body-style="{ padding: '0px' }" shadow="hover" style="height: 560px;padding:5px" >
                    <div  class="clearfix">
                        <img src="../../assets/img/icon-func.png" class="user-avator" alt />
                        <div class="resource-info-cont">系统功能
                        </div>
                        <el-input placeholder="请输入要搜索的功能" suffix-icon="el-icon-search" v-model="input2" style="width: 200px;margin-left:380px" > </el-input>
                    </div>
                    <hr style="border:2 dashed #987cb9" SIZE=1>
                    <div class="func-list">
                           <div class="func-list-box"  @click="tasktype()">
                            <img class="func-list-icon" src="../../assets/img/icon-newtask.png" />
                            <div class="func-list-name">新建任务</div>
                        </div>
                        <div class="func-list-box" style="padding-top:7px" @click="tasklist()">
                            <img class="func-list-icon"  src="../../assets/img/icon-taskdetail.png"  style="height:72px"/>
                            <div class="func-list-name">任务查看</div>
                        </div>
                                                <div class="func-list-box">
                            <img  class="func-list-icon" src="../../assets/img/icon-tasklist.png" />
                            <div class="func-list-name">任务列表</div>
                        </div>
                                                <div class="func-list-box">
                            <img class="func-list-icon"  src="../../assets/img/icon-usertask.png" @click="mytask()"/>
                            <div class="func-list-name">用户任务</div>
                        </div>
                                                <div class="func-list-box">
                            <img class="func-list-icon" src="../../assets/img/icon-rmanager.png" />
                            <div class="func-list-name">资源管理</div>
                        </div>
                                                <div class="func-list-box">
                            <img  class="func-list-icon" src="../../assets/img/icon-smanager.png" />
                            <div class="func-list-name">系统维护</div>
                        </div>
                                                <div class="func-list-box">
                            <img class="func-list-icon"  src="../../assets/img/icon-userinvite.png" />
                            <div class="func-list-name">用户邀请</div>
                        </div>
                                                <div class="func-list-box">
                            <img class="func-list-icon" src="../../assets/img/icon-crowd.png" />
                            <div class="func-list-name">众包接入</div>
                        </div>
                                                <div class="func-list-box">
                            <img  class="func-list-icon" src="../../assets/img/icon-app.png" />
                            <div class="func-list-name">自定义应用</div>
                        </div>
                                                <div class="func-list-box">
                            <img class="func-list-icon" src="../../assets/img/icon-systeminstall.png" />
                            <div class="func-list-name">系统设置</div>
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
            todoList: [
                {
                    title: '行为人重识别',
                    status: false
                },
                {
                    title: '假消息检测',
                    status: true
                }
            ],
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
        tasktype(){
                 this.$router.push('/tasktype');
        },
        tasklist(){
                 this.$router.push('/tasklist');
        },
        mytask(){
                 this.$router.push('/mytask');
        },
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
    background: url('../../assets/img/background1.png') no-repeat;
    background-size: 100% 100%;
    display: flex;
    align-items: center;
    padding: 10px;
    padding-right: 0px;
    border-bottom: 2px solid #ccc;
}

.user-avator {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    cursor: pointer;
}

.user-info-cont {
    width: 80px;
    height: 80px;
    background: url('../../assets/img/star-six.png') no-repeat;
    background-size: 100% 100%;
    font-size: 14px;
    color: white;
    margin-left: 50px;
    padding-top: 10px;
    text-align: center;
}

.user-info-cont div:first-child {
    font-size: 22px;
    color: #222;
    cursor: pointer;
}

.user-info-list {
    font-size: 14px;
    color: #999;
    line-height: 20px;
}

.user-info-list span {
    margin-left: 70px;
}

.mgb20 {
    margin-bottom: 20px;
    padding: 0px;
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
.information {
    margin-left: auto;
    height: 65px;
    width: 130px;
    line-height: 60px;
    background-color: pink;
    text-align: center;
    font-size: 22px;
    font-weight: 1000;
    border-radius: 50px;
    cursor: pointer;
}
.user-func {
    padding: 15px;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 180px;
    background-color: #d8d8d8;
}
.user-func-box {
    cursor: pointer;
}

.divider {
    margin: 0px 60px 0px 60px;
    width: 0;
    height: 100px;
    border-style: dashed;
    border-left: #848484;
}
.user-func-name {
    text-align: center;
    font-size: 18px;
    font-weight: 800;
}
.resource-info-cont {
    margin-left: 20px;
    font-size: 24px;
    font-weight: 1000;
    cursor: pointer;
}
.resource-info {
    background: linear-gradient(to right, rgba(255, 0, 0, 0), rgb(3, 102, 11));
    /* background: linear, left top, left bottom, color-stop(0, #ff4f02), color-stop(1, #8f2c00); */
    display: flex;
    align-items: center;
    padding: 10px;
    padding-right: 0px;
    border-bottom: 2px solid #ccc;
}
.clearfix{
    display: flex;
    align-items: center;
}
.func-list{
     display: flex;
     flex-wrap: wrap;
}
.func-list-box{
    height:100px;
    width:80px;
    margin:20px 60px 20px 60px;
    text-align: center;

}
.func-list-icon{
    width:80px;
    height:80px;
    cursor: pointer;
}
.func-list-name{
     cursor: pointer;
}

</style>
