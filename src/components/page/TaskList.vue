<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-lx-home"></i>任务列表</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <el-row :gutter="18">
            <el-col :span="24">
                <el-card shadow="hover" style="height: 580px" :body-style="{ padding: '0px' }">
                    <div class="header-box1">
                        <img src="../../assets/img/icon-typeinformation.png" style="width: 45px; height: 45px" />
                        <span style="color: white; font-size: 20px">任务列表</span>
                    </div>
                    <div class="tasklist-header">
                        <div class="search-box" style="float: left">
                            <span class="search-name">任务类型</span>
                            <el-select v-model="value1" clearable placeholder="请选择">
                                <el-option v-for="item in options1" :key="item.value1" :label="item.label" :value="item.value1">
                                </el-option>
                            </el-select>
                        </div>
                        <div class="search-box" style="float: left; margin-left: 0">
                            <span class="search-name">任务状态</span>
                            <el-select v-model="value2" clearable placeholder="请选择">
                                <el-option v-for="item in options2" :key="item.value2" :label="item.label" :value="item.value2">
                                </el-option>
                            </el-select>
                        </div>
                        <div class="search-box">
                            <span class="search-name">任务描述</span>
                            <el-input style="width: 187px" placeholder="请输入关键字" prefix-icon="el-icon-search" v-model="input">
                            </el-input>
                        </div>
                        <div class="search-box" style="float: left">
                            <span class="search-name">开始时间</span>
                            <el-date-picker
                                v-model="value3"
                                type="datetime"
                                placeholder="选择日期时间"
                                default-time="12:00:00"
                                style="width: 187px"
                            >
                            </el-date-picker>
                        </div>
                        <div class="search-box">
                            <span class="search-name">结束时间</span>
                            <el-date-picker
                                v-model="value4"
                                type="datetime"
                                placeholder="选择日期时间"
                                default-time="12:00:00"
                                style="width: 187px"
                            >
                            </el-date-picker>
                        </div>
                    </div>
                    <div style="display: flex; flex-wrap: wrap; flex-direction: row">
                        <task-box style="margin-top:20px" v-bind:detail="detail[0]"></task-box>
                        <task-box  v-bind:detail="detail[1]"></task-box>
                    </div>
                    <div class="page">
                        <el-pagination
                            @size-change="handleSizeChange"
                            @current-change="handleCurrentChange"
                            :current-page.sync="currentPage3"
                            :page-size="2"
                            layout="total, prev, pager, next, jumper"
                            :total="60"
                        >
                        </el-pagination>
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
import TaskBox from '../common/TaskBox.vue';
export default {
    name: 'dashboard',
    data: function () {
        return {
            radio: true,
            radio1: '1',
            radio2: '1',
            radio3: '1',
            value3: '',
            value4: '',
            input: '',
            detail:[
                {
                    type:"识别任务",
                    status:"执行中",
                    name:"嫌疑人识别",
                    time:"2020-12-20",
                    description:"从视频中获取嫌疑人目标所在图片帧并标注",
                    request:"4天 96%"
                },
                {
                    type:"识别任务",
                    status:"已完成",
                    name:"嫌疑人识别",
                    time:"2020-12-11",
                    description:"从视频中获取嫌疑人目标所在图片帧并标注",
                    request:"3天 95%"
                },
            ],
            options1: [
                {
                    value1: '分类任务',
                    label: '分类任务'
                },
                {
                    value1: '识别任务',
                    label: '识别任务'
                },
                {
                    value1: '生成任务',
                    label: '生成任务'
                },
                {
                    value1: '其他任务',
                    label: '其他任务'
                },
                {
                    value1: '所有任务',
                    label: '所有任务'
                }
            ],
            value1: '分类任务',
            options2: [
                {
                    value2: '已完成任务',
                    label: '已完成任务'
                },
                {
                    value2: '执行中任务',
                    label: '执行中任务'
                },
                {
                    value2: '未执行任务',
                    label: '未执行任务'
                },
                {
                    value2: '所有任务',
                    label: '所有任务'
                }
            ],
            value2: '执行中任务',
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
        VueCropper,
        TaskBox
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
        laststep() {
            this.$router.push('/identificationtask');
        },
        submittask() {
            this.$confirm('此操作将提交任务, 是否继续?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            })
                .then(() => {
                    this.$message({
                        type: 'success',
                        message: '提交成功!'
                    });
                    this.$router.push('/home');
                })
                .catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消提交'
                    });
                });
        }
    }
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
.tasktype1-header {
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    background: radial-gradient(rgba(185, 171, 171, 0), #ffb5c5);
    text-align: center;
    height: 120px;
    width: 40px;
    margin: 10px;
}
.tasktype2-header {
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    background: radial-gradient(rgba(185, 171, 171, 0), #aeeeee);
    text-align: center;
    height: 120px;
    width: 40px;
    margin: 10px;
}
.tasktype3-header {
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    background: radial-gradient(rgba(134, 94, 94, 0), #f5f25e);
    text-align: center;
    height: 120px;
    width: 40px;
    margin: 10px;
}
.tasktype1 {
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    background: radial-gradient(rgba(185, 171, 171, 0), #ffb5c5);
    text-align: center;
    height: 120px;
    width: 550px;
    margin: 10px;
}
.tasktype2 {
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    background: radial-gradient(rgba(185, 171, 171, 0), #aeeeee);
    text-align: center;
    height: 120px;
    width: 550px;
    margin: 10px;
}
.tasktype3 {
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    background: radial-gradient(rgba(134, 94, 94, 0), #f5f25e);
    text-align: center;
    height: 120px;
    width: 550px;
    margin: 10px;
}
.tasktype-name {
    font-size: 22px;
    font-weight: 800;
}
.typeinformation-title {
    font-size: 22px;
    font-weight: 800;
    margin-left: 10px;
}
.typeinformation-header {
    display: flex;
    align-items: center;
}
.typeinformation-name-box {
    display: flex;
    align-items: center;
}
.typeinformation-name1 {
    text-align: center;
    width: 95px;
    margin: 25px 15px 25px 15px;
    background-color: #ffb5c5;
    font-size: 18px;
    cursor: pointer;
}
.typeinformation-name2 {
    text-align: center;
    width: 95px;
    margin: 25px 15px 25px 15px;
    background-color: #aeeeee;
    font-size: 18px;
    cursor: pointer;
}
.typeinformation-name3 {
    text-align: center;
    width: 95px;
    margin: 25px 15px 25px 15px;
    background-color: #9aff9a;
    font-size: 18px;
    cursor: pointer;
}
.typeinformation-name4 {
    text-align: center;
    width: 95px;
    margin: 25px 15px 25px 15px;
    background-color: #bebebe;
    font-size: 18px;
    cursor: pointer;
}
.header-box1 {
    width: 200px;
    height: 50px;
    background: url('../../assets/img/icon-typebackground.png') no-repeat;
    background-size: 100% 100%;
    display: flex;
    align-items: center;
}
.header-box2 {
    width: 200px;
    height: 50px;
    background: url('../../assets/img/icon-typebackground.png') no-repeat;
    background-size: 100% 100%;
    display: flex;
    align-items: center;
}
.typeinformation-cont {
    padding: 15px;
}
.tasktype-box {
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    margin-left: 20px;
}
.div-header {
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    height: 10px;
    margin-left: 30px;
    width: 40px;
}
.div-choose {
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    height: 10px;
    width: 570px;
}
.next-btn {
    position: relative;
    width: 100px;
    height: 40px;
    line-height: 40px;
    padding: 0 25px;
    margin: 5px;
    background-color: #409eff;
    color: #fff;
    font-size: 14px;
    border-radius: 4px;
    box-sizing: border-box;
    cursor: pointer;
}
.submit-btn {
    position: relative;
    width: 100px;
    height: 40px;
    line-height: 40px;
    padding: 0 33px;
    margin: 5px;
    background-color: #409eff;
    color: #fff;
    font-size: 14px;
    border-radius: 4px;
    box-sizing: border-box;
    cursor: pointer;
}
.button-box {
    display: flex;
    align-items: center;
    justify-content: center;
}
.tasklist-header {
    height: 90px;
    background: url('../../assets/img/tasklist-header.png') no-repeat;
    background-size: 100% 100%;
    padding: 5px;
}
.search-box {
    margin-top: 5px;
    margin-left: 50px;
    margin-right: 50px;
    justify-items: center;
    display: flex;
    align-items: center;
}
.search-name {
    margin-right: 30px;
    font-size: 22px;
    font-weight: 800;
}
.page{
   margin-top: 10px;
   display:flex;
   justify-content:center;
   align-items: center;
}
</style>
