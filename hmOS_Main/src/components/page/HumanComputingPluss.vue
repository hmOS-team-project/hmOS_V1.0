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
        <el-row :gutter="18" style="margin: 30px 120px">
            <el-col :span="16">
                <el-card
                    shadow="hover"
                    style="height: 620px; padding: 5px; background-color: rgba(5, 53, 77, 0.7); border: 0"
                    :body-style="{ padding: '0px' }"
                >
                    <div class="header-box1">
                        <img src="../../assets/img/feedback.png" style="width: 45px; height: 45px" />
                        <span class="header-name">Operation Feedback</span>
                    </div>
                    <div class="divider div-transparent"></div>
                    <div
                        style="
                            float: left;
                            display: flex;
                            flex-direction: column;
                            text-align: center;
                            align-items: center;
                            margin: 100px 20px 20px 40px;
                        "
                    >
                        <span style="color: #03e9f4; font-size: 22px; font-weight: 600"> Query Photo </span>
                        <img :src="query" alt="" class="crop-img" />
                    </div>
                    <div class="card-stack">
                        <!-- <a class="buttons prev"><</a> -->
                        <ul class="card-list">
                            <li class="card" style="background: #00416a; background: linear-gradient(to right, #ffe000, #799f0c, #00416a)">
                                <img src="../../assets/img/executing.png" alt="" class="card-list__image" />

                                <!-- <h3 class="card-list__text">Relax and chill, we've got you covered :)</h3> -->
                            </li>
                            <li class="card" style="background: #1e3c72; background: linear-gradient(to right, #2a5298, #1e3c72)">
                                <img src="../../assets/img/executing.png" alt="" class="card-list__image" />
                            </li>
                            <li class="card" style="background: #2c3e50; background: linear-gradient(to right, #fd746c, #2c3e50)">
                                <img src="../../assets/img/executing.png" alt="" class="card-list__image" />
                            </li>
                            <li class="card" style="background: #373b44; background: linear-gradient(to right, #4286f4, #373b44)">
                                <img :src="person2" alt="" class="card-list__image" />
                            </li>
                            <li class="card activeNow" style="background: #c31432; background: linear-gradient(to right, #240b36, #c31432)">
                                <img :src="person1" alt="" class="card-list__image" />
                            </li>
                        </ul>
                        <a class="buttons next">&gt;</a>
                    </div>
                    <fieldset tabindex="0" class="radioGroup">
                        <!-- <legend>Cool radio buttons:</legend> -->
                        <input id="g1o1" name="group1" checked v-model="label" value="true" type="radio" />
                        <label for="g1o1">True</label>
                        <input id="g1o2" name="group1" value="false" v-model="label" type="radio" />
                        <label for="g1o2">False</label>
                    </fieldset>
                        <div class="next-btn3" style="margin-left:450px" @click="submitdataset()">
                                <a class="flowbutton"><span></span><span></span><span></span><span></span>Finished</a>
                            </div>
                    <!-- <div
                        style="
                            display: flex;
                            width: 225px;
                            height: 120px;
                            flex-wrap: wrap;
                            margin-top: 140px;
                            margin-left: 380px;
                            background-color: rgba(5, 53, 77, 0.7);
                        "
                    >
                        <div class="next-btn" style="margin-right: 0px">
                            <a class="flowbutton1"><span></span><span></span><span></span><span></span>Cancel</a>
                        </div>
                        <div class="next-btn" style="margin-left: 5px" @click="taskmode()">
                            <a class="flowbutton"><span></span><span></span><span></span><span></span>Save</a>
                        </div>
                    </div> -->
                </el-card>
            </el-col>
            <el-col :span="8">
                <el-card
                    shadow="hover"
                    style="height: 620px; padding: 5px; background-color: rgba(5, 53, 77, 0.7); border: 0"
                    :body-style="{ padding: '0px' }"
                >
                    <div class="header-box1">
                        <img src="../../assets/img/picture.png" style="width: 45px; height: 45px" />
                        <span class="header-name">Progress Display</span>
                    </div>
                    <div class="divider div-transparent"></div>
                    <div>
                        <img :src="url.url" style="height: 160px; width: 140px; margin-left: 10px" />
                        <div class="work-time">
                            <span>Work Time</span>
                            <span class="start-time">Start time：{{ start_time }}</span>
                            <span class="start-time">Time cost：{{ count_time }}</span>
                        </div>
                    </div>
                    <div style="display:flex;  align-items: center;flex-direction: column">
                    <div style="color: #03e9f4; font-size: 22px; font-weight: 600; margin-bottom: -60px; margin-top: 30px">
                        Pending Task
                    </div>
                    <div
                        style="
                            width: 225px;
                            height: 50px;
                            margin-top: 70px;
                            background-color: rgba(5, 53, 77, 0.7);
                            color: #FACC2E;
                            line-height:45px;
                            text-align:center;
                            font-size:55px;
                            font-weight:400
                        "
                    >
                        {{ taskNumber }}
                    </div>
                       <div style="color: #03e9f4; font-size: 22px; font-weight: 600; margin-bottom: -60px; margin-top: 30px">
                        Completed Task
                    </div>
                    <div
                        style="
                            width: 225px;
                            height: 50px;
                            margin-top: 70px;
                            background-color: rgba(5, 53, 77, 0.7);
                            color: #00FF80;
                            line-height:45px;
                            text-align:center;
                            font-size:55px;
                            font-weight:400
                        "
                    >
                        {{ completeTaskNum }}
                    </div>
                    <div style="color: #03e9f4; font-size: 22px; font-weight: 600; margin-bottom: -60px; margin-top: 30px">
                        Machine Has Done
                    </div>
                    <div
                        style="
                            width: 225px;
                            height: 50px;
                            margin-top: 70px;
                            background-color: rgba(5, 53, 77, 0.7);
                            color: #00FF80;
                            line-height:45px;
                            text-align:center;
                            font-size:55px;
                            font-weight:400
                        "
                    >
                        {{ ModelHasDone }}
                    </div>
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
import '@/assets/css/style.css';
import '@/assets/css/normalize.min.css';
import '@/assets/css/Datacages_Homeindex.css';
import '@/assets/js/jquery.min.js.下载';
import '@/assets/js/jquery.js.下载';
import Schart from 'vue-schart';
import VueCropper from 'vue-cropperjs';
export default {
    name: 'dashboard',
    data: function () {
        return {
            //  url: { url: require('../../assets/img/work.gif') },
            url: { url: require('../../assets/img/work.png') },
            person1: require('../../assets/img/executing.png'),
            person2: require('../../assets/img/executing.png'),
            query:'',
            ModelHasDone:'True',
            label: 'true',
            taskNumber: 0,
            completeTaskNum:0,
            start_time:
                new Date().getFullYear() +
                '-' +
                (new Date().getMonth() + 1) +
                '-' +
                new Date().getDate() +
                ' ' +
                new Date().getHours() +
                ':' +
                new Date().getMinutes() +
                ':' +
                new Date().getSeconds(),
            count_time: '00:00:00',
            content: ''
        };
    },
    components: {
        Schart,
        VueCropper
    },
    computed: {},

    methods: {
        submitdataset(){
            this.$router.push('/homeplus');
        },
        taskmode() {
            this.$router.push('/taskmodeplus');
        },
        changeDate() {
            const now = new Date().getTime();
            this.data.forEach((item, index) => {
                const date = new Date(now - (6 - index) * 86400000);
                item.name = `${date.getFullYear()}/${date.getMonth() + 1}/${date.getDate()}`;
            });
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
    mounted() {
        
        this.countTime(this.start_time);
        var $card = $('.card');
        var lastCard = $('.card-list .card').length - 1;
        let _this = this;
        // 调用时机根据需求
        setInterval(function () {
            _this.$axios.get('http://localhost:8005/getnum').then((res) => {
                console.log(res.data);
                _this.taskNumber = res.data;
            });
            _this.$axios.get('http://localhost:8005/getfinishtasknum').then((res) => {
                console.log(res.data);
                _this.completeTaskNum = res.data;
            });
            _this.$axios.get('http://localhost:8005/getstatus').then((res) => {
                console.log(res.data);
                _this.ModelHasDone = res.data;
            });
        }, 1000);
                let queryurl = JSON.parse(decodeURIComponent(this.$route.params.queryurl));
        this.$axios.post('http://localhost:2333/download/getquery', queryurl).then((res) => {
            if (res.data.code == 200) {
                this.query = res.data.queryUrl;
            } else {
                alert('Network is wrong！');
            }
        });
        let data = {};
        this.$axios.post('http://localhost:2333/download/single', data).then((res) => {
            if (res.data.code == 200) {
                this.person1 = res.data.url;
            } else {
                alert('Network is wrong！');
            }
        });
        $('.next').click(function () {
             $('.next').addClass("notclick");//设为不可点击
            //提交现在的标签并删除当前的照片
            let label = {
                label: _this.label
            };
            _this.$axios.post('http://localhost:2333/submitlabel', label).then((Res) => {
                ///任务数量减一
                _this.$axios.get('http://localhost:8005/feedback')
                   alert("submit successfully!!!")
                //取下一张照片并渲染
                _this.$axios.post('http://localhost:2333/download/single', data).then((res) => {
                    if (res.data.code == 200) {
                        _this.person2 = res.data.url;
                        var prependList = function () {
                            if ($('.card').hasClass('activeNow')) {
                                var $slicedCard = $('.card').slice(lastCard).removeClass('transformThis activeNow');
                                $('ul').prepend($slicedCard);
                            }
                        };
                        $('li').last().removeClass('transformPrev').addClass('transformThis').prev().addClass('activeNow');
                        $('.activeNow').children('img').attr('src', _this.person2);
                        setTimeout(function () {
                            prependList();
                        }, 100);
                         $('.next').removeClass("notclick");//设为不可点击
                    } else {
                        alert('Network is wrong！');
                    }
                });
            });

            //去取下一个照片
        });

        // $('.prev').click(function () {
        //     var appendToList = function () {
        //         if ($('.card').hasClass('activeNow')) {
        //             var $slicedCard = $('.card').slice(0, 1).addClass('transformPrev');
        //             $('.card-list').append($slicedCard);
        //         }
        //     };

        //     $('li').removeClass('transformPrev').last().addClass('activeNow').prevAll().removeClass('activeNow');
        //     setTimeout(function () {
        //         appendToList();
        //     }, 150);
        // });
    },
    beforeDestroy() {
        if (this.timer) {
            clearInterval(this.timer);
        }
    }
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
    margin-left: 10px;
}
.crop-demo {
    width: 300px;
    border: 2px solid gray;
    border-radius: 15px;
    padding: 5px;
    margin-top: 10px;
    margin-bottom: 10px;
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
.next-btn {
    position: relative;
    width: 100px;
    height: 40px;
    line-height: 40px;
    padding: 0 25px;
    margin-top: 25px;
    font-size: 14px;
    border-radius: 4px;
    box-sizing: border-box;
    cursor: pointer;
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
    margin-top: 10px;
}
.query_input {
    margin-left: 360px;
}
.crop-btn-box {
    margin-top: 18px;
    margin-right: 40px;
    float: right;
}
.header-box1 {
    width: 350px;
    height: 50px;
    /* background: url('../../assets/img/icon-typebackground.png') no-repeat; */
    background-size: 100% 100%;
    display: flex;
    align-items: center;
    margin-bottom: 10px;
}
.resource-box {
    display: flex;
    text-align: center;
    margin-left: 50px;
    margin-top: 35px;
}
.resourcenum {
    display: flex;
    flex-direction: column;
    text-align: center;
}
.number-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 60px;
}
.button-box {
    display: flex;
    align-items: center;
    justify-content: center;
}
.net-box {
    display: flex;
    align-items: center;
    padding: 5px;
    background: rgba(114, 160, 184, 0.2);
    margin: 20px 10px 20px 10px;
}
.net-name {
    display: flex;
    width: 100px;
    height: 50px;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    font-weight: 800;
    color: #03e9f4;
    text-align: center;
}
.net-select {
    width: 250px;
    height: 100px;
    padding-top: 7px;
    margin-left: 4px;
    display: flex;
    align-items: center;
}
.flowbutton {
    position: relative;
    display: inline-block;
    padding: 0px 0px;
    margin: 10px 0;
    color: #03e9f4;
    text-decoration: none;
    text-transform: uppercase;
    transition: 0.5s;
    letter-spacing: 1px;
    font-size: 28px;
    font-weight: 500;
    overflow: hidden;
}

.flowbutton:hover {
    background: #03e9f4;
    color: #050801;
    box-shadow: 0 0 5px #03e9f4, 0 0 25px #03e9f4, 0 0 50px #03e9f4, 0 0 200px #03e9f4;
    -webkit-box-reflect: below 1px linear-gradient(transparent, #0005);
}

.flowbutton span {
    position: absolute;
    display: block;
}

.flowbutton span:nth-child(1) {
    top: 0;
    left: 0;
    width: 100%;
    height: 3px;
    background: linear-gradient(90deg, transparent, #03e9f4);
    animation: animate1 1s linear infinite;
}

@keyframes animate1 {
    0% {
        left: -100%;
    }
    50%,
    100% {
        left: 100%;
    }
}

.flowbutton span:nth-child(2) {
    top: -100%;
    right: 0;
    width: 3px;
    height: 100%;
    background: linear-gradient(180deg, transparent, #03e9f4);
    animation: animate2 1s linear infinite;
    animation-delay: 0.25s;
}

@keyframes animate2 {
    0% {
        top: -100%;
    }
    50%,
    100% {
        top: 100%;
    }
}

.flowbutton span:nth-child(3) {
    bottom: 0;
    right: 0;
    width: 100%;
    height: 3px;
    background: linear-gradient(270deg, transparent, #03e9f4);
    animation: animate3 1s linear infinite;
    animation-delay: 0.5s;
}

@keyframes animate3 {
    0% {
        right: -100%;
    }
    50%,
    100% {
        right: 100%;
    }
}

.flowbutton span:nth-child(4) {
    bottom: -100%;
    left: 0;
    width: 3px;
    height: 100%;
    background: linear-gradient(360deg, transparent, #03e9f4);
    animation: animate4 1s linear infinite;
    animation-delay: 0.75s;
}

@keyframes animate4 {
    0% {
        bottom: -100%;
    }
    50%,
    100% {
        bottom: 100%;
    }
}
.flowbutton1 {
    position: relative;
    display: inline-block;
    padding: 0px 0px;
    margin: 10px 0;
    color: #03e9f4;
    text-decoration: none;
    text-transform: uppercase;
    transition: 0.5s;
    letter-spacing: 0px;
    font-size: 24px;
    font-weight: 500;
    overflow: hidden;
}

.flowbutton1:hover {
    background: #03e9f4;
    color: #050801;
    box-shadow: 0 0 5px #03e9f4, 0 0 25px #03e9f4, 0 0 50px #03e9f4, 0 0 200px #03e9f4;
    -webkit-box-reflect: below 1px linear-gradient(transparent, #0005);
}

.flowbutton1 span {
    position: absolute;
    display: block;
}

.flowbutton1 span:nth-child(1) {
    top: 0;
    left: 0;
    width: 100%;
    height: 3px;
    background: linear-gradient(90deg, transparent, #03e9f4);
    animation: animate1 1s linear infinite;
}
.header-name {
    color: rgb(0, 228, 255);
    margin-left: 20px;
    font-size: 24px;
    font-weight: 1000;
    cursor: pointer;
}
.form-item-name >>> .el-form-item__label {
    color: #03e9f4;
    line-height: 60px;
    font-size: 18px;
    font-weight: 400;
}

.input1 {
    border: 2px solid #03e9f4;
    font-size: 1.5em;
    padding: 0.25em 0.5em 0.3125em;
    color: #03e9f4;
    border-radius: 0.25em;
    /* background: transparent; */
    background: rgba(168, 184, 192, 0.2);
    -webkit-transition: all 0.1s;
    transition: all 0.1s;
    margin: 10px auto;
}

.input1:focus {
    outline: none;
    color: #03e9f4;
    border-color: #03e9f4;
}

.input1.keyup {
    color: white;
    border-color: white;
    text-shadow: 0 0 0.125em white;
    box-shadow: 0 0 0.25em white, inset 0 0 0.25em white;
}

canvas {
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    pointer-events: none;
}

.input1 {
    font-family: 'Arial Rounded MT Bold', 'Helvetica Rounded', Arial, sans-serif;
}

::input1-placeholder {
    color: #03e9f4;
    text-shadow: 0 0 0.125em transparent;
    -webkit-transition: all 0.25s;
    transition: all 0.25s;
}

.input1:focus::-webkit-input-placeholder {
    opacity: 0.5;
}

::-moz-placeholder {
    color: #03e9f4;
    text-shadow: 0 0 0.125em transparent;
    -webkit-transition: all 0.25s;
    transition: all 0.25s;
}

.input1:focus::-moz-placeholder {
    opacity: 0.5;
}

:-ms-input1-placeholder {
    color: #03e9f4;
    text-shadow: 0 0 0.125em transparent;
    -webkit-transition: all 0.25s;
    transition: all 0.25s;
}

.input1:focus:-ms-input-placeholder {
    opacity: 0.5;
}
.el-radio >>> .el-radio__inner {
    border-color: #03e9f4;
}
.el-radio >>> .el-radio__label {
    color: #03e9f4;
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
.container-box2 {
    vertical-align: top;
    display: inline-block;
    width: 320px;
    height: 400px;
    margin-top: 20px;
    margin-left: 70px;
    border-radius: 10%;
    /* background-color: black; */
    border: 3px dashed #c0c0c0;
}
.container-box2-header {
    margin-top: 10px;
    height: 50px;
    font-size: 24px;
    font-weight: 500;
    color: rgb(254, 67, 101);
    text-align: center;
}
.container1-box2-img {
    display: inline-flex;
    width: 120px;
    height: 150px;
    margin-left: 24px;
    margin-top: 5px;
}
.container-box1 {
    display: inline-block;
    vertical-align: top;
    width: 300px;
    height: 400px;
    margin-top: 20px;
    margin-left: 70px;
    border-radius: 10%;
    /* background-color: black; */
    border: 3px dashed #c0c0c0;
}
.container-box1-header {
    margin-top: 10px;
    height: 50px;
    font-size: 24px;
    font-weight: 500;
    color: rgb(100, 213, 114);
    text-align: center;
}
.container1-box1-img {
    display: inline-flex;
    width: 120px;
    height: 150px;
    margin-left: 16px;
    margin-top: 5px;
}
.grid-con-icon {
    vertical-align: middle;
    display: inline-block;
    margin-left: 350px;
    font-size: 36px;
    width: 40px;
    height: 40px;
    text-align: center;
    line-height: 40px;
    color: #03e9f4;
}

.grid-con-1 .grid-num {
    color: #03e9f4;
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
.work-time {
    background-color: rgba(5, 53, 77, 0.7);
    width: 240px;
    margin-top: 10px;
    vertical-align: top;
    display: inline-block;
    text-align: center;
    font-size: 24px;
    font-weight: 600;
    /* color: rgb(242, 94, 67); */
    color: #03e9f4;
}
.start-time {
    margin-top: 15px;
    display: block;
    width: 220px;
    font-size: 18px;
}
.crop-img {
    width: 150px;
    height: 200px;
}
.card-stack {
    width: 400px;
    height: 250px;
    position: relative;
    margin: 30px auto;
    margin-left: 300px;
}
.card-stack .buttons {
    display: none;
    position: absolute;
    background: rgba(0, 0, 0, 0.46);
    border: 2px solid rgba(255, 255, 255, 0.7);
    border-radius: 50%;
    width: 35px;
    height: 35px;
    left: 0;
    top: 55%;
    color: rgba(255, 255, 255, 0.7);
    text-align: center;
    line-height: 30px;
    text-decoration: none;
    font-size: 22px;
    z-index: 100;
    outline: none;
    transition: all 0.2s ease;
}
.card-stack .buttons:hover {
    transform: scale(1.3, 1.3);
}
.card-stack .prev {
    left: 15px;
    right: auto;
}
.card-stack .next {
    left: auto;
    right: 15px;
}
.card-stack .carousel .buttons:hover {
    color: #c01313;
    background: #fff;
}
.card-stack .card-list {
    width: 400px;
}
.card-stack .card-list__image {
    height: 200px;
}
.card-stack .card-list__text {
    color: #fff;
    font-weight: 300;
}
.card-stack .card-list li {
    display: flex;

    align-items: center;
    justify-content: center;
    transition: all 100ms ease-in-out;
    border-radius: 10px;
    position: absolute;
    list-style: none;
    height: 300px;
    left: 0;
    right: 0;
    margin: 0 auto;
    padding-top: 20px;
    text-align: center;
    box-shadow: 0 1px 4px 1px rgba(0, 0, 0, 0.5);
}
.card-stack .card-list li:nth-child(1) {
    top: 24px;
    width: 60%;
    /* animation: scaleCard 100ms; */
}
.card-stack .card-list li:nth-child(2) {
    top: 36px;
    width: 70%;
}
.card-stack .card-list li:nth-child(3) {
    top: 48px;
    width: 80%;
}
.card-stack .card-list li:nth-child(4) {
    top: 60px;
    width: 90%;
}
.card-stack .card-list li:nth-child(5) {
    top: 72px;
    width: 100%;
}
.card-stack:hover > .buttons.prev {
    display: block;
    animation: bounceInLeft 200ms;
}
.card-stack:hover > .buttons.next {
    display: block;
    animation: bounceInRight 200ms;
}
.transformThis {
    animation: scaleDown 500ms;
}
.transformPrev {
    animation: scaleUp 100ms;
    display: none;
}
@keyframes scaleUp {
    0% {
        transform: scale(1.2) translateY(50px);
        opacity: 0;
    }
    20% {
        transform: scale(1.15) translateY(40px);
        opacity: 0.1;
    }
    40% {
        transform: scale(1.1) translateY(30px);
        opacity: 0.2;
    }
    60% {
        transform: scale(1.05) translateY(20px);
        opacity: 0.4;
    }
    80% {
        transform: scale(1.01) translateY(10px);
        opacity: 0.8;
    }
    100% {
        transform: scale(1) translateY(0);
        opacity: 1;
    }
}
@keyframes scaleDown {
    0% {
        transform: scale(1) translateY(0);
        opacity: 1;
    }
    20% {
        transform: scale(1.01) translateY(20px);
        opacity: 0.8;
    }
    40% {
        transform: scale(1.05) translateY(40px);
        opacity: 0.4;
    }
    60% {
        transform: scale(1.1) translateY(60px);
        opacity: 0.2;
    }
    80% {
        transform: scale(1.15) translateY(80px);
        opacity: 0.1;
    }
    100% {
        transform: scale(1.2) translateY(100px);
        opacity: 0;
    }
}
@keyframes scaleCard {
    0% {
        top: 5px;
    }
    100% {
        top: 24px;
    }
}
@keyframes bounceInLeft {
    0% {
        opacity: 0;
        transform: translateX(40px);
    }
    100% {
        transform: translateX(0);
    }
}
@keyframes bounceInRight {
    0% {
        opacity: 0;
        transform: translateX(-40px);
    }
    100% {
        transform: translateX(0);
    }
}
.radioGroup {
    border: 0;
    font: 1.5em 'Roboto Condensed', arial;
    color: rgb(3, 233, 244);
    -webkit-transform: translateZ(0);
    -ms-transform: translateZ(0);
    -o-transform: translateZ(0);
    transform: translateZ(0);
    margin-top: 140px;
    margin-left: 400px;
}
.radioGroup > legend {
    color: #79eac5;
}
.radioGroup label {
    position: relative;
    padding-left: 1.3em;
    cursor: pointer;
    -webkit-transition: 0.2s;
    -o-transition: 0.2s;
    transition: 0.2s;
}
.radioGroup label:hover {
    color: #fff;
}
.radioGroup label::before,
.radioGroup label::after {
    content: '';
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    margin: auto;
    width: 1em;
    height: 1em;
    border-radius: 50%;
}
.radioGroup label::before {
    box-shadow: 0 1px 0 rgba(255, 255, 255, 0.25), 0 2px 5px 6px rgba(0, 0, 0, 0.5) inset;
}
.radioGroup label::after {
    background: #79eac5;
    opacity: 0.2;
    -webkit-transform: scale(0);
    -ms-transform: scale(0);
    -o-transform: scale(0);
    transform: scale(0);
    -webkit-transition: 0.3s;
    -o-transition: 0.3s;
    transition: 0.3s;
}
.radioGroup label:hover::after {
    -webkit-transform: scale(0.6);
    -ms-transform: scale(0.6);
    -o-transform: scale(0.6);
    transform: scale(0.6);
    opacity: 1;
    -webkit-transition: 0.2s;
    -o-transition: 0.2s;
    transition: 0.2s;
}
.radioGroup input {
    position: absolute;
    left: -24px;
    z-index: -1;
    opacity: 0;
}
.radioGroup input:checked + label::after {
    -webkit-transform: scale(0.8);
    -ms-transform: scale(0.8);
    -o-transform: scale(0.8);
    transform: scale(0.8);
    opacity: 1;
    box-shadow: 0 0 15px -1px #79eac5;
}
.notclick{
  pointer-events: none;
}
</style>