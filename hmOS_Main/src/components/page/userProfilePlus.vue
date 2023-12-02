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
            <el-col :span="24">
                <el-card
                    shadow="hover"
                    style="height: 620px; padding: 5px; background-color: rgba(50, 26, 50, 0.5); border: 0"
                    :body-style="{ padding: '0px' }"
                >
                    <div class="header-box1">
                        <img src="../../assets/img/mytasks.png" style="width: 45px; height: 45px" />
                        <span class="header-name">My Profile</span>
                    </div>
                    <div class="divider div-transparent"></div>
                    <el-col :span="8" style="width: 960px">
                        <el-card
                            :body-style="{ padding: '0px' }"
                            shadow="hover"
                            style="
                                height: 450px;
                                background-color: rgba(3, 26, 37, 0.4);
                                border: 0px;
                                position: fixed;
                                top: 50px;
                                left: 200px;
                                right: 200px;
                                bottom: 0px;
                                margin: auto;
                            "
                        >
                            <el-row>
                                <el-col :span="8">
                                    <span class="title-text" style="margin-left: 200px; top: 10px">User name</span>
                                </el-col>
                                <el-col :span="8">
                                    <el-input v-model="username" placeholder="请输入内容" size="medium" style="margin-top: 10px"></el-input>
                                </el-col>
                            </el-row>
                            <el-row>
                                <el-col :span="8">
                                    <span class="title-text" style="margin-left: 200px; top: 10px">Email</span>
                                </el-col>
                                <el-col :span="8">
                                    <el-input
                                        v-model="email"
                                        placeholder="请输入内容"
                                        size="medium"
                                        style="margin-top: 10px"
                                        :disabled="true"
                                    ></el-input>
                                </el-col>
                            </el-row>
                            <el-row>
                                <el-col :span="8">
                                    <span class="title-text" style="margin-left: 200px; top: 10px">Telephone</span>
                                </el-col>
                                <el-col :span="8">
                                    <el-input
                                        v-model="phoneNumber"
                                        placeholder="请输入内容"
                                        size="medium"
                                        style="margin-top: 10px"
                                    ></el-input>
                                </el-col>
                            </el-row>
                            <el-row>
                                <el-col :span="8">
                                    <span class="title-text" style="margin-left: 200px; top: 10px">Address</span>
                                </el-col>
                                <el-col :span="8">
                                    <el-input v-model="address" placeholder="请输入内容" size="medium" style="margin-top: 10px"></el-input>
                                </el-col>
                            </el-row>
                            <el-row>
                                <el-col :span="8">
                                    <span class="title-text" style="margin-left: 200px; top: 10px">Gender</span>
                                </el-col>
                                <el-col :span="8">
                                    <div style="top: 15px">
                                        <el-radio v-model="gender" label="0">Male</el-radio>
                                        <el-radio v-model="gender" label="1">Female</el-radio>
                                    </div>
                                </el-col>
                            </el-row>
                            <div class="send-btn" @click="sendEdit()">
                                <a class="flowbutton"><span></span><span></span><span></span><span></span>Confirm</a>
                            </div>
                        </el-card>
                    </el-col>
                </el-card>
            </el-col>
        </el-row>
        <!-- <div class="mouser"></div> -->
        <div class="copyrigntoutbox" style="position: relative; top: -22px">
            <span class="copyrigntmsg">Copyright © 2021 Northwestern Polytechnical University All Rights Reserved</span>
        </div>
    </div>
</template>
<script>
import '@/assets/css/style.css';
import '@/assets/css/normalize.min.css';
import '@/assets/js/index.js.下载';
import '@/assets/css/Datacages_Homeindex.css';
import '@/assets/js/jwt-decode.js';
export default {
    data: function () {
        return {
            input: '',
            radio: 'male',
            username: '',
            email: '',
            phoneNumber: '',
            address: '',
            gender: ''
        };
    },
    methods: {
        getCurrentUser(id) {
            this.$axios.get('http://localhost:3000/api/user/edit', id).then((res) => {
                var currentUser = res.data.user;
                this.username = currentUser.username;
                this.email = currentUser.email;
                this.phoneNumber = currentUser.telephone;
                this.address = currentUser.address;
                this.gender = currentUser.sex.toString();
            });
        },
        sendEdit() {
            let newUser = {
                name: this.username,
                email: this.email,
                telephone: this.phoneNumber,
                address: this.address,
                sex: parseInt(this.gender)
            };
            this.$axios.post('http://localhost:3000/api/user/edit', newUser).then((res) => {
                if (res.data.success === 0) {
                    window.alert('Server err,please try again!');
                } else {
                    localStorage.setItem('Authorization', res.data.token);
                    this.$router.push('/homeplus');
                }
            });
        }
    },
    mounted() {
        var token = localStorage.Authorization;
        var decode = jwt_decode(token);
        this.getCurrentUser(decode.id);
    },
    created: function () {}
};
</script>

<style scoped>
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
.header-name {
    color: rgb(0, 228, 255);
    margin-left: 20px;
    font-size: 24px;
    font-weight: 1000;
    cursor: pointer;
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
.post {
    display: block;
    font-size: 15px;
}
.title-text {
    color: rgb(0, 228, 255);
    margin-left: px;
    font-size: 20px;
    font-weight: 200;
    cursor: pointer;
}
.send-btn {
    position: relative;
    width: 300px;
    height: 30px;
    line-height: 40px;
    padding: 0 10px;
    margin-top: 70px;
    font-size: 10px;
    border-radius: 4px;
    box-sizing: border-box;
    cursor: pointer;
    margin-left: 450px;
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
    letter-spacing: 4px;
    font-size: 30px;
    font-weight: 500;
    overflow: hidden;
    margin-right: 50px;
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
</style>