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
                    style="height: 620px; padding: 5px; background-color: rgba(1, 0, 191, 0.5); border: 0"
                    :body-style="{ padding: '0px' }"
                >
                    <div class="header-box1">
                        <img src="../../assets/img/taskview.png" style="width: 45px; height: 45px" />
                        <span class="header-name">Task View</span>
                    </div>
                    <div class="divider div-transparent"></div>
                    <el-row :gutter="20" style="margin-left: 15px"> </el-row>
                    <el-form
                        ref="form"
                        :model="form"
                        label-width="160px"
                        class="form-item-name"
                        style="background-color: rgba(0, 168, 255, 0.2); height: 105px; padding: 5px"
                    >
                        <div class="search-box" style="float: left">
                            <span class="search-name">Task Type</span>
                            <el-select v-model="value1" clearable placeholder="choose">
                                <el-option v-for="item in options1" :key="item.value1" :label="item.label" :value="item.value1">
                                </el-option>
                            </el-select>
                        </div>
                        <div class="search-box" style="float: left; margin-left: 0">
                            <span class="search-name">Task State</span>
                            <el-select v-model="value2" clearable placeholder="choose">
                                <el-option v-for="item in options2" :key="item.value2" :label="item.label" :value="item.value2">
                                </el-option>
                            </el-select>
                        </div>
                        <div class="search-box">
                            <span class="search-name">Task Description</span>
                            <el-input style="width: 200px" placeholder="keyword" prefix-icon="el-icon-search" v-model="input"> </el-input>
                        </div>
                        <div class="search-box" style="float: left">
                            <span class="search-name">Start Time</span>
                            <el-date-picker
                                v-model="value3"
                                type="datetime"
                                placeholder="choose date"
                                default-time="12:00:00"
                                style="width: 187px"
                            >
                            </el-date-picker>
                        </div>
                        <div class="search-box" style="float: left; margin-left: 0">
                            <span class="search-name">End Time</span>
                            <el-date-picker
                                v-model="value4"
                                type="datetime"
                                placeholder="choose date"
                                default-time="12:00:00"
                                style="width: 187px"
                            >
                            </el-date-picker>
                        </div>
                    </el-form>
                    <div style="display: flex; flex-wrap: wrap; flex-direction: row">
                        <task-box style="margin-top: 20px" v-bind:detail="taskList[0]"></task-box>
                        <task-box v-bind:detail="taskList[1]"></task-box>
                    </div>
                    <div class="page">
                        <el-pagination
                            @size-change="handleSizeChange"
                            @current-change="handleCurrentChange"
                            :current-page.sync="currentPage3"
                            :page-size="2"
                            layout="total, prev, pager, next, jumper"
                            :total="60"
                            background="rgba(0, 168, 255, 0.2)"
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
export default {
    name: 'dashboard',
    data: function () {
        return {
            taskList: [],
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
            value1: 'Classification',
            options2: [
                {
                    value2: 'Completed',
                    label: 'Completed'
                },
                {
                    value2: 'Executing',
                    label: 'Executing'
                },
                {
                    value2: 'Waiting',
                    label: 'Waiting'
                },
                {
                    value2: 'All',
                    label: 'All'
                }
            ],
            value2: 'Executing',
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
    mounted:function(){
        this.getTaskList();
    },
    methods: {
        getTaskList() {
            this.$axios.get('http://localhost:3000/api/task/getalltask').then((res) => {
                if (res.data.success == 1) {
                    this.taskList = res.data.Tasklist;
                } else {
                    console.log('请求数据失败！');
                }
            });
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