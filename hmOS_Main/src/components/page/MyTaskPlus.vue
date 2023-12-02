<template>
    <div>
        <!--?-->
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
        <el-row :gutter="18" style="margin: 30px 120px">
            <el-col :span="24">
                <el-card
                    shadow="hover"
                    style="height: 620px; padding: 5px; background-color: rgba(5, 53, 77, 0.7); border: 0"
                    :body-style="{ padding: '0px' }"
                >
                    <div class="header-box1">
                        <img src="../../assets/img/mytasks.png" style="width: 45px; height: 45px" />
                        <span class="header-name">My Task</span>
                    </div>
                    <div class="divider div-transparent"></div>
                    <el-row :gutter="20" style="margin-left: 15px"> </el-row>
                    <el-form
                        ref="form"
                        :model="form"
                        label-width="160px"
                        class="form-item-name"
                        style="
                            background-color: rgba(3, 26, 37, 0.4);
                            height: 105px;
                            padding: 5px;
                            box-shadow: 0px 0px 10px #837979;
                            border-radius: 10px;
                        "
                    >
                        <div class="search-box" style="float: left">
                            <span class="search-name">Task Type</span>
                            <el-select id="selectType" v-model="value1" clearable @change="searchByTaskType" placeholder="choose">
                                <el-option v-for="item in options1" :key="item.value1" :label="item.label" :value="item.value1">
                                </el-option>
                            </el-select>
                        </div>
                        <div class="search-box" style="float: left; margin-left: 0">
                            <span class="search-name">Task State</span>
                            <el-select id="selectState" v-model="value2" clearable @change="searchByTaskState" placeholder="choose">
                                <el-option v-for="item in options2" :key="item.value2" :label="item.label" :value="item.value2">
                                </el-option>
                            </el-select>
                        </div>
                        <div class="search-box">
                            <span class="search-name">Create Time</span>
                            <el-date-picker
                                id="selectDate"
                                v-model="value3"
                                type="date"
                                placeholder="choose date"
                                default-time="12:00:00"
                                style="width: 187px"
                                @change="searchByDate"
                            >
                            </el-date-picker>
                        </div>
                        <div class="search-box">
                            <span class="search-name">Task Description</span>
                            <el-input
                                id="inputDescription"
                                style="width: 200px"
                                placeholder="keyword"
                                prefix-icon="el-icon-search"
                                v-model="input"
                            >
                            </el-input>
                            <el-button style="margin-left: 10px" icon="el-icon-search" type="primary" @click="searchByDescription"
                                >search</el-button
                            >
                        </div>
                    </el-form>
                    <div style="display: flex; flex-wrap: wrap; flex-direction: row">
                        <task-box
                            style="margin-top: 20px"
                            v-bind:detail="taskList.slice((currentPage - 1) * pageSize, currentPage * pageSize)[0]"
                        ></task-box>
                        <task-box v-bind:detail="taskList.slice((currentPage - 1) * pageSize, currentPage * pageSize)[1]"></task-box>
                    </div>
                    <div class="page">
                        <el-pagination
                            @size-change="handleSizeChange"
                            @current-change="handleCurrentChange"
                            :current-page="currentPage"
                            :page-size="pageSize"
                            layout="total, prev, pager, next, jumper"
                            :total="totalCount"
                            background="rgba(5, 53, 77, 0.7)"
                        >
                        </el-pagination>
                    </div>
                </el-card>
            </el-col>
        </el-row>
        <div class="copyrigntoutbox" style="position: relative; top: -22px">
            <span class="copyrigntmsg">Copyright © 2021 Northwestern Polytechnical University All Rights Reserved</span>
        </div>
    </div>
</template>

<script>
import TaskBox from '../common/TaskBox.vue';
import '@/assets/css/Datacages_Homeindex.css';
import '@/assets/js/jwt-decode.js';
export default {
    name: 'dashboard',
    data: function () {
        return {
            pageList: [],
            taskList: [], //任务列表
            currentPage: 1, //默认显示第一页
            totalCount: 60, //数据总数
            pageSize: 2, //每页显示数据条数
            radio: true,
            radio1: '1',
            radio2: '1',
            radio3: '1',
            value3: '',
            value4: '',
            input: '',
            options1: [
                {
                    value1: 'Classification',
                    label: 'Classification'
                },
                {
                    value1: 'Identification',
                    label: 'Identification'
                },
                {
                    value1: 'Generation',
                    label: 'Generation'
                },
                {
                    value1: 'Others',
                    label: 'Others'
                },
                {
                    value1: 'All Tasks',
                    label: 'All Tasks'
                }
            ],
            value1: 'All Tasks',
            options2: [
                {
                    value2: 'Unexecuted',
                    label: 'Unexecuted'
                },
                {
                    value2: 'Executing',
                    label: 'Executing'
                },
                {
                    value2: 'Finished',
                    label: 'Finished'
                },
                {
                    value2: 'All',
                    label: 'All'
                }
            ],
            value2: 'All',
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
        TaskBox
    },
    created: function () {
        var token = localStorage.Authorization;
        var decode = jwt_decode(token);
        var userId = decode.id;
        this.getMyTaskList(userId);
    },
    methods: {
        getMyTaskList(userId) {
            let data = {
                id: userId
            };
            console.log(data);
            this.$axios.post('http://localhost:3000/api/task/getmytask', data).then((res) => {
                if (res.data.success == 1) {
                    this.taskList = res.data.Tasklist;
                } else {
                    console.log('请求数据失败！');
                }
            });
        },
        handleSizeChange(val) {
            //每次切换页面大小时，此方法改变页面大小
            this.pageSize = val;
            this.currentPage = 1;
        },
        handleCurrentChange(val) {
            //每次切面当前页时，此方法相应改变当前页
            this.currentPage = val;
        },
        searchByTaskType(val) {
            //val为所选的Type类型
            this.resetSelect();
            if (val == 'All Tasks') {
                this.getTaskList();
            } else {
                let data = {
                    taskType: val
                };
                this.$axios.post('http://localhost:3000/api/task/searchbytype', data).then((res) => {
                    if (res.data.success == 1) {
                        this.taskList = res.data.list;
                    } else {
                        console.log('请求数据失败！');
                    }
                });
            }
        },
        searchByTaskState(val) {
            this.resetSelect();
            if (val == 'All') {
                this.getTaskList();
            } else {
                let data = {
                    taskStatus: val
                };
                this.$axios.post('http://localhost:3000/api/task/searchbystate', data).then((res) => {
                    if (res.data.success == 1) {
                        this.taskList = res.data.list;
                    } else {
                        console.log('请求数据失败！');
                    }
                });
            }
        },
        searchByDate(val) {
            this.resetSelect();
            let date = val.getFullYear() + '-' + (val.getMonth() + 1) + '-' + val.getDate();
            let data = {
                startTime: date
            };
            this.$axios.post('http://localhost:3000/api/task/searchbydate', data).then((res) => {
                if (res.data.success == 1) {
                    this.taskList = res.data.list;
                } else {
                    console.log('请求数据失败！');
                }
            });
        },
        searchByDescription() {
            console.log(document.getElementById('inputDescription').value);
            let data = {
                description: document.getElementById('inputDescription').value
            };
            this.$axios.post('http://localhost:3000/api/task/searchbydescription', data).then((res) => {
                if (res.data.success == 1) {
                    this.taskList = res.data.list;
                } else {
                    console.log('请求数据失败！');
                }
            });
            this.resetSelect();
        },
        resetSelect() {
            document.getElementById('selectType').value = 'All Tasks';
            document.getElementById('selectState').value = 'All';
            document.getElementById('selectDate').value = null;
            document.getElementById('inputDescription').value = null;
        }
    }
};
</script>

<style>
.header-name {
    color: rgb(0, 228, 255);
    margin-left: 20px;
    font-size: 24px;
    font-weight: 1000;
    cursor: pointer;
}
.header-box1 {
    width: 300px;
    height: 50px;
    background-size: 100% 100%;
    display: flex;
    align-items: center;
    margin-bottom: 10px;
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
.search-box {
    margin-top: 5px;
    margin-left: 50px;
    margin-right: 50px;
    justify-items: center;
    display: flex;
    align-items: center;
}
.search-name {
    color: rgb(0, 228, 255);
    margin-right: 30px;
    font-size: 22px;
    font-weight: 800;
}
.page {
    margin-top: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
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
</style>