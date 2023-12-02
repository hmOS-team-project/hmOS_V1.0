<template>
    <div id="bg" class="bg">
        <vue-particles
            color="#fff"
            :particleOpacity="0.7"
            :particlesNumber="60"
            shapeType="circle"
            :particleSize="4"
            linesColor="#fff"
            :linesWidth="1"
            :lineLinked="true"
            :lineOpacity="0.4"
            :linesDistance="150"
            :moveSpeed="2"
            :hoverEffect="true"
            hoverMode="grab"
            :clickEffect="true"
            clickMode="push"
            class="lizi"
        >
        </vue-particles>
        <canvas class="pg-canvas" width="1536" height="760"></canvas>
        <div class="login">
            <div class="login_title">
                <span>SIGN UP</span>
            </div>
            <div class="login_fields">
                <div class="login_fields__user">
                    <div class="icon" style="opacity: 0.5">
                        <img alt="" src="@/assets/img/user_icon_copy.png" />
                    </div>
                    <input name="login" placeholder="Input Username" v-model="username" maxlength="16" type="text" autocomplete="off" />
                    <div class="validation">
                        <img alt="" src="@/assets/img/tick.png" />
                    </div>
                </div>
                <div class="login_fields__password">
                    <div class="icon">
                        <img alt="" src="@/assets/img/email_icon.png" />
                    </div>
                    <input name="email" placeholder="Input Email" v-model="email" maxlength="20" type="text" autocomplete="off" />
                    <div class="validation">
                        <img alt="" src="@/assets/img/tick.png" />
                    </div>
                </div>
                <div class="login_fields__password">
                    <div class="icon">
                        <img alt="" src="@/assets/img/lock_icon_copy.png" />
                    </div>
                    <input name="pwd" placeholder="Input Password" v-model="password" maxlength="10" type="password" autocomplete="off" />
                    <div class="validation">
                        <img alt="" src="@/assets/img/tick.png" />
                    </div>
                </div>
                <div class="login_fields__submit">
                    <input type="button" id="login_button" value="Sign in" @click="userLogin" />
                </div>
                <div class="login_fields__register">
                    <input type="button" id="register_button" value="Sign up" />
                </div>
            </div>
            <div class="success"></div>
            <div class="disclaimer">
                <p>© Human-Machine Computing Group</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data: function () {
        return {
            username: '',
            email: '',
            password: ''
        };
    },
    methods: {
        userLogin() {
            this.$router.push('/login');
        }
    },
    mounted() {
        var _this = this;
        $('input[id="register_button"]').click(function () {
            var username = $('input[name="login"]').val();
            var email = $('input[name="email"]').val();
            var pwd = $('input[name="pwd"]').val();
            if (username == '') {
                alert('Please input your username!');
            } else if (email == '') {
                alert('Please input your Email!');
            } else if (pwd == '') {
                alert('Please input your password!');
            } else {
                //认证中..
                $('.login').addClass('test'); //倾斜特效
                setTimeout(function () {
                    $('.login').addClass('testtwo'); //平移特效
                }, 300);
                setTimeout(function () {
                    $('.authent').show().animate(
                        { right: -320 },
                        {
                            easing: 'easeOutQuint',
                            duration: 600,
                            queue: false
                        }
                    );
                    $('.authent')
                        .animate(
                            { opacity: 1 },
                            {
                                duration: 200,
                                queue: false
                            }
                        )
                        .addClass('visible');
                }, 500);
                setTimeout(function () {
                    $('.authent').show().animate(
                        { right: 90 },
                        {
                            easing: 'easeOutQuint',
                            duration: 600,
                            queue: false
                        }
                    );
                    $('.authent')
                        .animate(
                            { opacity: 0 },
                            {
                                duration: 200,
                                queue: false
                            }
                        )
                        .addClass('visible');
                }, 1000);
                let user = {
                    username: _this.username,
                    email: _this.email,
                    password: _this.password
                };
                _this.$axios
                    .post('http://localhost:3000/api/user/register', user)
                    .then((res) => {
                        //ajax返回
                        //认证完成
                        setTimeout(function () {
                            $('.authent').show().animate(
                                { right: 90 },
                                {
                                    easing: 'easeOutQuint',
                                    duration: 600,
                                    queue: false
                                }
                            );
                            $('.authent')
                                .animate(
                                    { opacity: 0 },
                                    {
                                        duration: 200,
                                        queue: false
                                    }
                                )
                                .addClass('visible');
                            $('.login').removeClass('testtwo'); //平移特效
                        }, 2000);
                        setTimeout(function () {
                            $('.authent').hide();
                            $('.login').removeClass('test');

                            var status_code = res.data.status_code;
                            if (status_code === 0) {
                                //注册成功
                                $('.login div').fadeOut(100);
                                $('.success').fadeIn(1000);
                                localStorage.setItem('Authorization', res.data.token);
                                _this.$router.push('/homeplus');
                                //跳转操作
                            } else if (status_code === 1) {
                                window.alert('Email already exists!');
                            } else if (status_code === 500) {
                                window.alert('Server is busy');
                            }
                        }, 2400);
                    })
                    .catch((error) => {
                        alert('Network is wrong');
                        setTimeout(function () {
                            $('.authent').show().animate(
                                { right: 90 },
                                {
                                    easing: 'easeOutQuint',
                                    duration: 600,
                                    queue: false
                                }
                            );
                            $('.authent')
                                .animate(
                                    { opacity: 0 },
                                    {
                                        duration: 200,
                                        queue: false
                                    }
                                )
                                .addClass('visible');
                            $('.login').removeClass('testtwo'); //平移特效
                        }, 10);
                        setTimeout(function () {
                            $('.authent').hide();
                            $('.login').removeClass('test');
                        }, 10);
                    });
            }
        });
    }
};
</script>


<style>
.authent {
    box-shadow: 0px 20px 30px 3px rgba(0, 0, 0, 0.55);
    display: none;
    background: #35394a;
    /* Old browsers */
    /* FF3.6+ */
    /* Chrome10+,Safari5.1+ */
    /* Opera 11.10+ */
    /* IE10+ */
    background: linear-gradient(230deg, rgba(53, 57, 74, 0) 0%, rgb(0, 0, 0) 100%);
    /* W3C */
    filter: progid: DXImageTransform.Microsoft.gradient( startColorstr='rgba(53, 57, 74, 0)', endColorstr='rgb(0, 0, 0)', GradientType=1);
    /* IE6-9 fallback on horizontal gradient */
    position: absolute;
    left: 0;
    right: 90px;
    margin: auto;
    width: 200px;
    color: white;
    text-transform: uppercase;
    letter-spacing: 1px;
    text-align: center;
    padding: 20px 70px;
    top: 200px;
    bottom: 0;
    height: 70px;
    opacity: 0;
}

.authent p {
    display: block;
    text-align: center;
    color: white;
}
.testtwo {
    left: -320px !important;
}

.test {
    box-shadow: 0px 20px 30px 3px rgba(0, 0, 0, 0.55);
    pointer-events: none;
    top: -100px !important;
    -webkit-transform: rotateX(70deg) scale(0.8) !important;
    transform: rotateX(70deg) scale(0.8) !important;
    opacity: 0.6 !important;
    -webkit-filter: blur(1px);
    filter: blur(1px);
}
.bg {
    padding: 0;
    margin: 0;
    height: 100%;
    font-size: 16px;
    background-repeat: no-repeat;
    background-position: left top;
    background-color: #242645;
    color: #fff;
    font-family: 'Source Sans Pro';
    background-size: 100%;
    background-image: url('../../assets/img/loginbg.png');
}
p {
    color: #d3d7f7;
    font-size: 10px;
    text-align: left;
}
.login {
    box-shadow: -15px 15px 15px rgba(6, 17, 47, 0.7);
    opacity: 1;
    top: 20px;
    -webkit-transition-timing-function: cubic-bezier(0.68, -0.25, 0.265, 0.85);
    -webkit-transition-property: -webkit-transform, opacity, box-shadow, top, left;
    transition-property: transform, opacity, box-shadow, top, left;
    -webkit-transition-duration: 0.5s;
    transition-duration: 0.5s;
    -webkit-transform-origin: 161px 100%;
    -ms-transform-origin: 161px 100%;
    transform-origin: 161px 100%;
    -webkit-transform: rotateX(0deg);
    transform: rotateX(0deg);
    position: relative;
    width: 340px;
    /*border-top: 2px solid #D8312A;*/
    height: 430px;
    position: absolute;
    left: 1000px;
    right: 0;
    margin: auto;
    top: 0;
    bottom: 0;
    padding: 60px 40px 40px 40px;
    background: #35394a;
    /* Old browsers */
    /* FF3.6+ */
    background: gradient(linear, left bottom, right top, color-stop(0%, #35394a), color-stop(100%, rgb(0, 0, 0)));
    /* Chrome,Safari4+ */
    background: linear-gradient(230deg, rgba(53, 57, 74, 0) 0%, rgb(0, 0, 0) 100%);
    /* Chrome10+,Safari5.1+ */
    /* Opera 11.10+ */
    /* IE10+ */
    background: linear-gradient(230deg, rgba(53, 57, 74, 0) 0%, rgb(0, 0, 0) 100%);
    /* W3C */
    filter: progid: DXImageTransform.Microsoft.gradient( startColorstr='rgba(53, 57, 74, 0)', endColorstr='rgb(0, 0, 0)', GradientType=1);
    /* IE6-9 fallback on horizontal gradient */
}

.login .validation {
    position: absolute;
    z-index: 1;
    right: 10px;
    top: 14px;
    opacity: 0;
}

.login .disclaimer {
    position: absolute;
    bottom: 20px;
    left: 35px;
    width: 250px;
}

.login .disclaimer p {
    text-align: center;
}

.login_title {
    color: #d3d7f7;
    height: 60px;
    text-align: left;
    font-size: 16px;
}

.login_fields {
    height: 208px;
    position: absolute;
    left: 0;
}

.login_fields .icon {
    position: absolute;
    z-index: 1;
    left: 36px;
    top: 8px;
    opacity: 0.5;
}

.login_fields input[type='password'],
.login_fields input[type='text'] {
    color: #61bfff !important;
}

.login_fields input[type='text'],
.login_fields input[type='password'] {
    color: #afb1be;
    width: 300px;
    margin-top: -2px;
    background: rgba(57, 61, 82, 0);
    left: 0;
    padding: 10px 65px;
    border-top: 2px solid rgba(57, 61, 82, 0);
    border-bottom: 2px solid rgba(57, 61, 82, 0);
    border-right: none;
    border-left: none;
    outline: none;
    font-family: 'Microsoft Yahei', sans-serif;
    box-shadow: none;
}

.login_fields__user,
.login_fields__eamil,
.login_fields__password {
    position: relative;
}

.login_fields__submit {
    float: left;
    margin-top: 10px;
    margin-left: 20px;
    width: 34%;
    right: 0;
}

.login_fields__register {
    float: left;
    margin-top: 10px;
    margin-left: 40px;
    width: 30%;
    right: 0;
}

.login_fields__register input {
    border-radius: 50px;
    background: transparent;
    padding: 10px 50px;
    border: 2px solid #4fa1d9;
    color: #4fa1d9;
    text-transform: uppercase;
    font-size: 11px;
    -webkit-transition-property: background, color;
    transition-property: background, color;
    -webkit-transition-duration: 0.2s;
    transition-duration: 0.2s;
}

.login_fields__submit .forgot {
    float: right;
    font-size: 10px;
    margin-top: 11px;
    text-decoration: underline;
}

.login_fields__submit .forgot a {
    color: #606479;
}
.login_fields__register .forgot {
    float: right;
    font-size: 10px;
    margin-top: 11px;
    text-decoration: underline;
}

.login_fields__register .forgot a {
    color: #606479;
}
.login_fields__submit input {
    border-radius: 50px;
    background: transparent;
    padding: 10px 50px;
    border: 2px solid #4fa1d9;
    color: #4fa1d9;
    text-transform: uppercase;
    font-size: 11px;
    -webkit-transition-property: background, color;
    transition-property: background, color;
    -webkit-transition-duration: 0.2s;
    transition-duration: 0.2s;
}

.login_fields__submit input:focus {
    box-shadow: none;
    outline: none;
}

.login_fields__submit input:hover {
    color: white;
    background: #4fa1d9;
    cursor: pointer;
    -webkit-transition-property: background, color;
    transition-property: background, color;
    -webkit-transition-duration: 0.2s;
    transition-duration: 0.2s;
}
.login_fields__register input:focus {
    box-shadow: none;
    outline: none;
}

.login_fields__register input:hover {
    color: white;
    background: #4fa1d9;
    cursor: pointer;
    -webkit-transition-property: background, color;
    transition-property: background, color;
    -webkit-transition-duration: 0.2s;
    transition-duration: 0.2s;
}
.success {
    display: none;
    color: #d5d8e2;
}

.success p {
    font-size: 14px;
}
</style>