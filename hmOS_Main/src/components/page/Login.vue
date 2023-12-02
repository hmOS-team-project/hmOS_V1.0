<template>
    <div class="background">
        <div class="el-row" style="margin: 0px 50px 32px; color: rgb(35, 103, 177); font-size: 33px">
            <img height="50px" src="@/assets/img/logo.png" style="position: relative; top: 7px" />
        <div class="verticalline"></div>
        </div>
            <div class="logo">
        <b>人机融合计算系统</b>
    </div>
        <div class="el-row" style="height: 480px">
            <div class="background1"></div>
            <div class="car-cover" style="top: 0px; transform: none"></div>
            <div style="width: 300px; height: 370px; z-index: 5; position: absolute; top: 50px; right: 0px">
                <div class="sw-login-main" style="top: 0px; transform: none">
                    <div class="sw-login-main-content">
                        <div class="card">
                            <ul
                                role="menubar"
                                class="sw-login-menu el-menu--horizontal el-menu"
                                style="background-color: rgba(255, 255, 255, 0)"
                            >
                                <li
                                    role="menuitem"
                                    tabindex="0"
                                    class="el-menu-item is-active"
                                    style="
                                        color: rgb(51, 148, 225);
                                        border-bottom-color: rgb(51, 148, 225);
                                        background-color: rgba(255, 255, 255, 0);
                                        margin: 0px 20px;
                                    "
                                >
                                    Username
                                </li>
                                <li
                                    role="menuitem"
                                    tabindex="0"
                                    class="el-menu-item"
                                    style="
                                        color: rgb(102, 102, 102);
                                        border-bottom-color: transparent;
                                        background-color: rgba(255, 255, 255, 0);
                                        margin: 0px 0px 0px 20px;
                                    "
                                >
                                    Dynamic Code
                                </li>
                            </ul>
                            <div style="">
                                <form class="el-form" id="fm1" style="margin: 20px" ref="login">
                                    <div class="el-form-item el-form-item--small" style="margin-bottom: 15px" prop="username">
                                        <div class="el-form-item__content">
                                            <div class="">
                                                        <el-input
                                                            v-model="param.username" placeholder="Enter your Username"
                                                            id="username"
                                                            size="25"
                                                            tabindex="1"
                                                            type="text"
                                                            autocomplete="off"
                                                            name="username"
                                                            value=""
                                                           >
                                                         <el-button slot="prepend" icon="el-icon-lx-people"></el-button>
                                                         </el-input>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="el-form-item el-form-item--small" style="margin-bottom: 15px" prop="password">
                                        <div class="el-form-item__content">
                                            <div class="">
                                                <div>
                                                    <el-input
                                                       v-model="param.password" placeholder="Enter your Password"
                                                        type="password"
                                                        id="password"
                                                        size="25"
                                                        tabindex="2"
                                                        accesskey="p"
                                                        autocomplete="off"
                                                        name="password"
                                                        value=""
                                                        >
                                                        <el-button slot="prepend" icon="el-icon-lock"></el-button>
                                                        </el-input>
                                                </div>
                                                <span class="el-input__suffix">
                                                    <span class="el-input__suffix-inner" style="display: inline-block">
                                                        <i
                                                            onclick="javascript: togglePassword(this);"
                                                            class="el-input__icon su-icon-hide el-input__clear"
                                                            style="line-height: 32px"
                                                        ></i> </span></span>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="el-form-item el-form-item--small" style="margin-bottom: 10px">
                                        <div class="el-form-item__content">
                                            <el-checkbox id="rememberMe" >
                                         Remember Me
                                            </el-checkbox>
                                            <a
                                                href="/cas/personal/forgotYourPassword"
                                                target="_blank"
                                                style="font-size: 14px; float: right; color: rgb(35, 103, 177); text-decoration-line: none"
                                                >Forgot your password?</a
                                            >
                                             <a href="/cas/personal/forgotYourPassword"
                                     target="_blank"
                                    style="font-size: 14px; float: right; color: rgb(35, 103, 177); text-decoration-line: none;"
                            >Active your account！</a>
                                        </div>
                                    </div>
                                    <div class="el-form-item el-form-item--small" style="margin-bottom: 10px">
                                        <div class="el-form-item__content">
                                            <input type="hidden" name="currentMenu" value="1" />
                                            <input type="hidden" name="execution" value="e1s1" />
                                            <input type="hidden" name="_eventId" value="submit" />
                                            <input type="hidden" name="geolocation" />
                                            <input
                                                name="submit"
                                                accesskey="l"
                                                tabindex="6"
                                                type="button"
                                                value="LOGIN"
                                                class="el-button el-button--primary el-button--small is-round"
                                                style="width: 100%; height: 40px; font-size: 16px"
                                                @click="submitForm()"
                                            />
                                        </div>
                                    </div>
                                </form>
                            </div>
                            <div style="display: none">
                                <form class="el-form" id="fm2" action="" style="margin: 20px">
                                    <div class="el-form-item el-form-item--small" style="margin-bottom: 15px">
                                        <div class="el-form-item__content">
                                            <div class="sw-input el-input el-input--default el-input--prefix sw-input--circular">
                                                <div>
                                                    <input
                                                        placeholder="Enter your Mobile"
                                                        title="Enter your Mobile"
                                                        id="username"
                                                        size="25"
                                                        tabindex="1"
                                                        type="text"
                                                        accesskey="m"
                                                        autocomplete="off"
                                                        name="username"
                                                        value=""
                                                        class="el-input__inner"
                                                    />
                                                </div>
                                                <span class="el-input__prefix">
                                                    <i class="su-input-icon black su-input-icon-prefix el-input__icon su-icon-people"></i>
                                                </span>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="el-form-item el-form-item--small" style="margin-bottom: 15px">
                                        <div class="el-form-item__content">
                                            <div
                                                class="sw-input su-input-text-button el-input el-input--defualt el-input-group el-input-group--append el-input--prefix sw-input--circular"
                                            >
                                                <el-input
                                                    placeholder="Enter the Dynamic Code"
                                                    title="Enter the Dynamic Code"
                                                    type="password"
                                                    id="password"
                                                    size="25"
                                                    tabindex="2"
                                                    accesskey="d"
                                                    autocomplete="off"
                                                    name="password"
                                                    value=""
                                                    class="el-input__inner"
                                                />
                                                <span class="el-input__prefix">
                                                    <i class="su-input-icon black su-input-icon-prefix el-input__icon su-icon-dyncode"></i>
                                                </span>
                                                <span class="el-input__suffix" style="right: 97px">
                                                    <span class="el-input__suffix-inner" style="display: inline-block">
                                                        <i
                                                            onclick="javascript: togglePassword(this);"
                                                            class="el-input__icon el-input__clear su-icon-hide"
                                                            style="line-height: 32px"
                                                        ></i> </span
                                                ></span>
                                                <div class="el-input-group__append">
                                                    <button
                                                        type="button"
                                                        class="el-button el-button--default el-button--small"
                                                    >
                                                        <span>Send</span>
                                                    </button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="el-form-item el-form-item--small" style="margin-bottom: 10px">
                                        <div class="el-form-item__content">
                                            <input type="hidden" name="currentMenu" value="2" />
                                            <input type="hidden" name="execution" value="e1s1" />
                                            <input type="hidden" name="_eventId" value="submitPasswordlessToken" />
                                            <input type="hidden" name="geolocation" />
                                            <input
                                                name="submit"
                                                accesskey="l"
                                                tabindex="6"
                                                type="button"
                                                value="LOGIN"
                                                style="width: 100%; height: 40px; font-size: 16px"
                                            />
                                        </div>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
           <div class="el-row" style="margin: 50px 50px 32px; color: rgb(35, 103, 177); font-size: 33px">
            <p>2020-2020 © 西北工业大学普适计算实验室</p>
        </div>
    </div>
        <!-- <div class="login-wrap">
            <div class="ms-login">
                <div class="ms-title">LOGIN</div>
                <el-form :model="param" :rules="rules" ref="login" label-width="0px" class="ms-content">
                    <el-form-item prop="username">
                        <el-input v-model="param.username" placeholder="username">
                            <el-button slot="prepend" icon="el-icon-lx-people"></el-button>
                        </el-input>
                    </el-form-item>
                    <el-form-item prop="password">
                        <el-input
                            type="password"
                            placeholder="password"
                            v-model="param.password"
                            @keyup.enter.native="submitForm()"
                        >
                            <el-button slot="prepend" icon="el-icon-lx-lock"></el-button>
                        </el-input>
                    </el-form-item>
                    <div class="login-btn">
                        <el-button type="primary" @click="submitForm()">登录</el-button>
                    </div>
                    <p class="login-tips"></p>
                </el-form>
            </div>
        </div> -->

    <!-- <body style="background-color:lightgray;">
    <div id="logo-image">
        <img src="../../assets/img/logo.png" alt="加载失败" >
    </div>
    <div class="verticalline"></div>
    <div id="logo">
        <b>人机融合计算系统</b>
    </div>

    <div id="hm-image">
        <img src="../../assets/img/hm_image.jpg" alt="加载失败" >
    </div>
    <div id="nwpu-image">
        <img src="../../assets/img/nwpu_bg.jpg" alt="加载失败" >
    </div>

    <div id="content_login">
        <div id="content-header">
            <h1>用户登录</h1>
        </div>
        <div class="container-fluid">
            <div class="row-fluid">
                <div class="span12">
                    <div class="widget-box">
                        <div class="widget-content nopadding">
                            <form action="" method="post" class="form-horizontal" id="visitquery">
                                <div class="control-group" >
                                    <label class="  " >用户名称：</label>
                                    <div class="controls">
                                        <input id="uid" type="text" />
                                    </div>
                                </div>
                                <div class="control-group" >
                                    <label class="control-label" >登录密码：</label>
                                    <div class="controls" >
                                        <input id="pwd" type="text" />
                                    </div>
                                </div>
                                <div class="form-actions" align="right">
                                    <button type="button" class="btn btn-primary" onclick="queryid(0);">登录</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div id="footer-login" class="span12">
            2020 - 2020 &copy; 西北工业大学普适计算实验室
    </div>
    </body> -->
</template>
<script>

export default {
    data: function () {
        return {
            param: {
                username: 'admin',
                password: '123123',
            },
            // rules: {
            //     username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
            //     password: [{ required: true, message: '请输入密码', trigger: 'blur' }]
            // }
        };
    },
    methods: {
        submitForm() {
            localStorage.setItem('ms_username', this.param.username);
            this.$router.push('/');
            // this.$refs.login.validate((valid) => {
            //     if (valid) {
            //         this.$message.success('登录成功');
            //         localStorage.setItem('ms_username', this.param.username);
            //         this.$router.push('/');
            //     } else {
            //         this.$message.error('请输入账号和密码');
            //         console.log('error submit!!');
            //         return false;
            //     }
            // });
        }
    }
};
</script>

<style scoped>
/* .login-wrap {
    position: relative;
    width: 100%;
    height: 100%;
    background-image: url(../../assets/img/login-bg1.jpg);
    background-size: 100%;
}
.ms-title {
    width: 100%;
    line-height: 50px;
    text-align: center;
    font-size: 20px;
    color: #fff;
    border-bottom: 1px solid #ddd;
}
.ms-login {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 350px;
    margin: -190px 0 0 -175px;
    border-radius: 5px;
    background: rgba(255, 255, 255, 0.3);
    overflow: hidden;
}
.ms-content {
    padding: 30px 30px;
}
.login-btn {
    text-align: center;
}
.login-btn button {
    width: 100%;
    height: 36px;
    margin-bottom: 10px;
}
.login-tips {
    font-size: 12px;
    line-height: 30px;
    color: #fff;
} */
.background{
     width: 100vw;
    height: 100vh;
    background: url(../../assets/img/bg.jpg) left center / cover no-repeat;
    padding-top:50px
}
.background1 {
    width: 100%;
    position: relative;
    background: url(../../assets/img/hm_image.jpg) left center / cover no-repeat;
    height: 480px;
}
.qq_style {
    margin: 0px 5px;
    font-size: 30px;
    display: inline-block;
    width: 30px;
    height: 30px;
    border-radius: 30px;
    cursor: pointer;
}
.wechat_style {
    margin: 0px 5px;
    font-size: 30px;
    display: inline-block;
    width: 30px;
    height: 30px;
    border-radius: 30px;
    cursor: pointer;
}
p {
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 600px;
    margin-inline-end: 0px;
    color: rgba(2, 21, 37, 0.65);
    font-size: 12px;
}
.logo{
	left: 345px;
    top: 60px;
	font-size: 30px;
	color:royalblue;
	position: absolute;
}
.verticalline{
	display: inline-block;
	width: 3px;
	height: 40px;
	left: 280px;
	top: 15px;
	position: absolute;
	background: #948e8e;
}

</style>