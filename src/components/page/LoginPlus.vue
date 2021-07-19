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
                <span>SIGN IN</span>
            </div>
            <div class="login_fields">
                <div class="login_fields__user">
                    <div class="icon" style="opacity: 0.5">
                        <img alt="" src="@/assets/img/user_icon_copy.png" />
                    </div>
                    <input name="login" placeholder="Username" v-model="username" maxlength="16" type="text" autocomplete="off" />
                    <div class="validation">
                        <img alt="" src="@/assets/img/tick.png" />
                    </div>
                </div>
                <div class="login_fields__password">
                    <div class="icon">
                        <img alt="" src="@/assets/img/lock_icon_copy.png" />
                    </div>
                    <input name="pwd" placeholder="Password" v-model="password" maxlength="16" type="password" autocomplete="off" />
                    <div class="validation">
                        <img alt="" src="@/assets/img/tick.png" />
                    </div>
                </div>
                <div class="login_fields__password">
                    <div class="icon">
                        <img alt="" src="@/assets/img/key.png" />
                    </div>
                    <input name="code" placeholder="Verification Code" maxlength="4" type="text" autocomplete="off" />
                    <div class="validation" style="opacity: 1; right: 0px; top: -3px">
                        <canvas class="J_codeimg" id="myCanvas">对不起，您的浏览器不支持canvas，请下载最新版浏览器!</canvas>
                    </div>
                </div>
                <div class="login_fields__submit">
                    <input type="button" id="login_button" value="Sign in" />
                </div>
                <div class="login_fields__register">
                    <input type="button" id="register_button" value="Sign up" @click="userRegister" />
                </div>
            </div>
            <div class="success"></div>
            <div class="disclaimer">
                <p>© Human-Machine Computing Group</p>
            </div>
        </div>
        <div class="authent">
            <div class="loader" style="height: 10px; width: 20px; margin-left: 50px">
                <div class="loader-inner ball-clip-rotate-multiple">
                    <div></div>
                    <div></div>
                    <div></div>
                </div>
            </div>
            <p>Authenticating...</p>
        </div>
        <div class="OverWindows"></div>
    </div>
</template>
<script>
// import '@/assets/css/styles.css';
// import '@/assets/css/demo.css';
import '@/assets/css/loaders.css';
import '@/assets/js/jquery.min.js.下载';
import '@/assets/js/jquery-ui.min.js.下载';
import '@/assets/js/stopExecutionOnTimeout.js.下载';
import '@/assets/js/Particleground.js.下载';
import '@/assets/js/Treatment.js.下载';
import '@/assets/js/jquery.mockjax.js.下载';
export default {
    data: function () {
        return {
            username: '',
            password: '',
            CodeVal: ''
        };
    },
    methods: {
        //用户注册
        userRegister() {
            this.$router.push('/register');
        }
    },

    mounted() {
        var canGetCookie = 0; //是否支持存储Cookie 0 不支持 1 支持
        var ajaxmockjax = 1; //是否启用虚拟Ajax的请求响 0 不启用  1 启用
        //默认账号密码
        var CodeVal = 0;
        Code();
        $('canvas[id="myCanvas"]').click(function () {
            Code();
        });
        function Code() {
            if (canGetCookie == 1) {
                createCode('AdminCode');
                var AdminCode = getCookieValue('AdminCode');
                showCheck(AdminCode);
            } else {
                showCheck(createCode());
            }
        }
        function createCode() {
            var code = '';
            var codeLength = 4; //验证码的长度
            var random = new Array(
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                'A',
                'B',
                'C',
                'D',
                'E',
                'F',
                'G',
                'H',
                'I',
                'J',
                'K',
                'L',
                'M',
                'N',
                'O',
                'P',
                'Q',
                'R',
                'S',
                'T',
                'U',
                'V',
                'W',
                'X',
                'Y',
                'Z'
            ); //随机数
            for (var i = 0; i < codeLength; i++) {
                //循环操作
                var index = Math.floor(Math.random() * 36); //取得随机数的				索引（0~35）
                code += random[index]; //根据索引取得随机数加到code上
            }
            return code;
        }
        function showCheck(a) {
            CodeVal = a;
            var c = document.getElementById('myCanvas');
            var ctx = c.getContext('2d');
            ctx.clearRect(0, 0, 1000, 1000);
            ctx.font = "80px 'Hiragino Sans GB'";
            ctx.fillStyle = '#E8DFE8';
            ctx.fillText(a, 0, 100);
        }
        $(document).keypress(function (e) {
            // 回车键事件
            if (e.which == 13) {
                $('input[id="login_button"]').click();
            }
        });

        $('input[name="pwd"]').focus(function () {
            $(this).attr('type', 'password');
        });
        $('input[type="text"]').focus(function () {
            $(this).prev().animate({ opacity: '1' }, 200);
        });
        $('input[type="text"],input[type="password"]').blur(function () {
            $(this).prev().animate({ opacity: '.5' }, 200);
        });
        $('input[name="login"],input[name="pwd"]').keyup(function () {
            var Len = $(this).val().length;
            if (!$(this).val() == '' && Len >= 5) {
                $(this).next().animate(
                    {
                        opacity: '1',
                        right: '30'
                    },
                    200
                );
            } else {
                $(this).next().animate(
                    {
                        opacity: '0',
                        right: '20'
                    },
                    200
                );
            }
        });
        //非空验证
        var _this = this;
        $('input[id="login_button"]').click(function () {
            var login = $('input[name="login"]').val();
            var pwd = $('input[name="pwd"]').val();
            var code = $('input[name="code"]').val();
            if (login == '') {
                alert('Please input your username!');
            } else if (pwd == '') {
                alert('Please input your password!');
            } else if (code == '') {
                alert('Please input Verification Code!');
            } else if (code != CodeVal) {
                alert('Verification Code is wrong!');
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
                let data = {
                    username: _this.username,
                    password: _this.password
                };
                _this.$axios
                    .post('http://localhost:3000/api/user/login', data)
                    .then((res) => {
                        console.log(res.data);
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
                            if (res.data.success) {
                                //登录成功
                                $('.login div').fadeOut(100);
                                $('.success').fadeIn(1000);
                                localStorage.setItem('Authorization', res.data.token);
                                _this.$router.push('/homeplus');
                                //跳转操作
                            } else {
                                alert('Username or password is wrong');
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
<style scoped>
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

.success {
    display: none;
    color: #d5d8e2;
}

.success p {
    font-size: 14px;
}

p {
    color: #d3d7f7;
    font-size: 10px;
    text-align: left;
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
.login_fields__password {
    position: relative;
}

.login_fields__submit {
    float: left;
    top: 17px;
    margin-left: 20px;
    width: 34%;
    right: 0;
}

.login_fields__register {
    float: left;
    top: 17px;
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
/* Color Schemes */

.love {
    position: absolute;
    right: 20px;
    bottom: 0px;
    font-size: 11px;
    font-weight: normal;
}

.love p {
    color: white;
    font-weight: normal;
    font-family: 'Open Sans', sans-serif;
}

.love a {
    color: white;
    font-weight: 700;
    text-decoration: none;
}

.love img {
    position: relative;
    top: 3px;
    margin: 0px 4px;
    width: 10px;
}

.brand {
    position: absolute;
    left: 20px;
    bottom: 14px;
}

.brand img {
    width: 30px;
}
/**
*
*
*/

:-moz-placeholder {
    /* Mozilla Firefox 4 to 18 */
    color: #cecfd2;
    opacity: 1;
}

::-moz-placeholder {
    /* Mozilla Firefox 19+ */
    color: #cecfd2;
    opacity: 1;
}

input:-ms-input-placeholder {
    color: #cecfd2;
    opacity: 1;
}

input::-webkit-input-placeholder {
    color: #cecfd2;
    opacity: 1;
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

h1 {
    font-size: 2.8em;
    font-weight: 700;
    letter-spacing: -1px;
    margin: 0.6rem 0;
}

h1 > span {
    font-weight: 300;
}

h2 {
    font-size: 1.15em;
    font-weight: 300;
    margin: 0.3rem 0;
}

main {
    width: 95%;
    max-width: 1000px;
    margin: 4em auto;
    opacity: 0;
}

main.loaded {
    transition: opacity 0.25s linear;
    opacity: 1;
}

main header {
    width: 100%;
}

main header > div {
    width: 50%;
}

main header > .left,
main header > .right {
    height: 100%;
}

main .loaders {
    width: 100%;
    box-sizing: border-box;
    display: flex;
    flex: 0 1 auto;
    flex-direction: row;
    flex-wrap: wrap;
}

main .loaders .loader {
    box-sizing: border-box;
    display: flex;
    flex: 0 1 auto;
    flex-direction: column;
    flex-grow: 1;
    flex-shrink: 0;
    flex-basis: 25%;
    max-width: 25%;
    height: 200px;
    align-items: center;
    justify-content: center;
}

.J_codeimg {
    width: 90px;
    height: 50px;
    padding: 3px;
    z-index: 0;
    color: #fff;
}
</style>