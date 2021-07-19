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
        <div class="container-box">
        <el-card
                :body-style="{ padding: '0px' }"
                shadow="hover"
                style=" background-color: rgba(1, 0, 191, 0.2); border: 0"
        >
            <div class="header-box1">
                <img src="../../assets/img/Crowdsourcing.png" style="width: 45px; height: 45px" />
                <span class="header-name">Crowdsourcing Accessing</span>
            </div>
        <el-row :gutter="50" style="margin-top: 30px; margin-left: 50px; margin-right: 50px; opacity: 0.9">
            <el-col :span="8">
                <el-card shadow="hover" style="height: 580px; border: 0" :body-style="{ padding: '0px' }">
                    <div class="header-text">
                        <img src="../../assets/img/Linklogo.png" style="width: 40px; height: 40px; left: -10px" />
                        <span >cloudcrowd</span>
                    </div>
                    <div class="header-box2" style="opacity: 1">
                        <img src="../../assets/img/Cloudcrowdlogo.png" style="width: 80%; height: 100%; margin: auto" />
                    </div>
                    <div id="frozen-btn">
                        <button class="yellow">ccrowd</button>
                    </div>
                </el-card>
            </el-col>
            <el-col :span="8">
                <el-card shadow="hover" style=" height: 580px; border: 0" :body-style="{ padding: '0px' }">
                    <div class="header-text">
                        <img src="../../assets/img/Linklogo.png" style="width: 40px; height: 40px; left: -10px" />
                        <span >Amazon mechanical turk</span>
                    </div>
                    <div class="header-box2" style="opacity: 1">
                        <img src="../../assets/img/AMTlogo.png" style="width: 60%; height: 90%; margin: auto" />
                    </div>
                    <div id="frozen-btn">
                        <button class="green">AMTurk</button>
                    </div>
                </el-card>
            </el-col>
            <el-col :span="8">
                <el-card shadow="hover" style=" height: 580px; border: 0" :body-style="{ padding: '0px' }">
                    <div class="header-text">
                        <img src="../../assets/img/Linklogo.png" style="width: 40px; height: 40px; left: -10px" />
                        <span >crowdflower</span>
                    </div>
                    <div class="header-box2" style="opacity: 1">
                        <img src="../../assets/img/crowdflower.png" style="width: 80%; height: 60%; margin: auto" />
                    </div>
                    <div id="frozen-btn">
                        <button class="purple">cflower</button>
                    </div>
                </el-card>
            </el-col>
        </el-row>
        </el-card>
        </div>

        <div class="copyrigntoutbox">
            <span class="copyrigntmsg">Copyright © 2021 Northwestern Polytechnical University All Rights Reserved </span>
        </div>
    </div>
</template>

<script>
    import '@/assets/css/style.css';
    import '@/assets/css/normalize.min.css';
    import '@/assets/js/index.js.下载';
    import '@/assets/css/Datacages_Homeindex.css';
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
                detail: [
                    {
                        type: 'Identification',
                        status: 'executing',
                        name: 'suspect classification',
                        time: '2020-12-20',
                        description: 'Get the suspect target from the video in the picture frame and labeled',
                        request: '4days 96%'
                    },
                    {
                        type: 'Identification',
                        status: 'completed',
                        name: 'suspect classification',
                        time: '2020-12-11',
                        description: 'Get the suspect target from the video in the picture frame and labeled',
                        request: '3days 95%'
                    }
                ],
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

    .user-info-cont div:first-child {
        font-size: 30px;
        color: #222;
    }

    .user-info-list span {
        margin-left: 70px;
    }

    .header-name {
        color: rgb(0, 228, 255);
        margin-left: 20px;
        font-size: 24px;
        font-weight: 1000;
        cursor: pointer;
    }
    .container-box{
        width: 1600px;
        height: 750px;
        margin: auto;
        margin-top: 50px;
        background: rgba(1, 0, 191, 0.5);
        background-repeat: no-repeat;
        background-size: 100% 100%;
        background-position: center;
        position: relative
    }
    .header-box1 {
        width: 100%;
        height: 50px;
        background-size: 100% 100%;
        display: flex;
        align-items: center;
        margin-top: 20px;
        margin-left: 20px;
        margin-bottom: 10px;
    }

    .header-box2 {
        width: 100%;
        height: 100px;
        margin: auto;
        background: rgb(255, 255, 255);
        background-repeat: no-repeat;
        background-size: 100% 100%;
        background-position: center;
        display: flex;
        align-items: center;
    }

    .header-text {
        content: '';
        border: 0;
        width: 100%;
        height: 70px;
        background: rgba(0, 100, 255, 0.9);
        text-transform: uppercase;
        font-size: 20px;
        font-weight: bold;
        padding:20px 0;
        text-align: center;
        color: white;
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
    .progress {
        margin-top: 30px;
    }

    .down_span {
        color: #dfdede;
        font-size: 12px;
        font-weight: lighter;
    }

    h3,
    ul,
    li {
        margin: 0;
        padding: 0;
        list-style: none;
    }

    .box-content {
        color: #fff;
        text-align: center;
        width: 80%;
        height: 80%;
        transform: translateX(-50%) translateY(-50%) scale(1);
        position: absolute;
        left: 30%;
        top: 50%;
        z-index: 2;
        transition: all 0.3s ease 0.5s;
    }

    .content {
        opacity: 0;
        transform: translateX(-50%) translateY(-50%);
        position: absolute;
        left: 50%;
        top: 50%;
        z-index: 3;
        transition: all 0.3s ease 0s;
        overflow-y: hidden;
    }

    .post {
        color: #000;
        font-size: 13px;
        font-weight: 500;
        letter-spacing: 1px;
        text-transform: capitalize;
        display: inline-block;
        margin-bottom: 10px;
        opacity: 0;
        transform: translateY(-500px);
        transition: all 0.8s ease 0.15s;
    }
    .tile:hover .content {
        opacity: 1;
    }
    .tile:hover .title,
    .tile:hover .post {
        opacity: 1;
        transform: translateY(0);
    }
    .title {
        color: #ff3a6f;
        font-size: 22px;
        font-weight: 600;
        text-transform: uppercase;
        transform: translateY(-500px);
        opacity: 0;
        transition: all 0.8s ease 0.3s;
    }

    /* 冰冻效果 */
    #frozen-btn button {
        border: 0;
        width: 100%;
        text-transform: uppercase;
        font-size: 50px;
        font-weight: bold;
        padding: 180px 120px;
        text-align: center;
        color: black;
        outline: none;
        position: relative;
    }

    #frozen-btn button:before {
        content: '';
        display: block;
        background: linear-gradient(to left, rgba(255, 255, 255, 0) 50%, rgba(255, 255, 255, 0.4) 50%);
        background-size: 210% 100%;
        background-position: right bottom;
        height: 100%;
        width: 100%;
        position: absolute;
        top: 0;
        bottom: 0;
        right: 0;
        left: 0;
        transition: all 1s;
        -webkit-transition: all 1s;
    }

    #frozen-btn .green {
        background-image: linear-gradient(to right, #25aae1, #40e495);
        box-shadow: 0 4px 15px 0 rgba(49, 196, 190, 0.75);
    }

    #frozen-btn .purple {
        background-image: linear-gradient(to right, #6253e1, #852D91);
        box-shadow: 0 4px 15px 0 rgba(236, 116, 149, 0.75);
    }

    #frozen-btn .yellow {
        background-image: linear-gradient(to right, #ffaa00, #ff5500);
        box-shadow: 0 4px 15px 0 rgba(255, 0, 85, 0.75);
    }

    #frozen-btn .purple:hover:before {
        background-position: left bottom;
    }

    #frozen-btn .green:hover:before {
        background-position: left bottom;
    }

    #frozen-btn .yellow:hover:before {
        background-position: left bottom;
    }
</style>