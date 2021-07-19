<template>
    <div>
        <div id="loading" style="display: none">
            <div class="loadEffect">
                <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
            </div>
        </div>
        <!--标题栏-->
            <div class="Hometitlebox">
       <img src="../../assets/img/logo2.png"   style="width:50px;height:50px;margin-right:25px"/>
            <a style="color: #00e4ff">hmOS1.0</a>
             <img src="../../assets/img/logo1.png" style="width:60px;height:50px;margin-left:15px"/>
            </div>
        <!--动效显示-->
 <div id="app1">
        <div class="tiles">
            <div class="type1 tile" style="--color: #FDBBBA" >
                <header>Classification</header>
                       <div class="box-content">
                        <div class="content">
                            <h3 class="title">For example</h3>
                            <span class="post">Multiclass</span>
                            <span class="post">Multilabels</span>
                            <span class="post">Imbalance</span>
                        </div>
                    </div>
            </div>
            <div class="type2 tile" style="--color: #CE98BC" @click="gotoIdentification()">
                <header>Identification</header>
                                      <div class="box-content">
                        <div class="content">
                            <h3 class="title">For example</h3>
                            <span class="post">Image Type</span>
                            <span class="post">Text Type</span>
                            <span class="post">Voice Type</span>
                        </div>
                    </div>
            </div>
            <div class="type3 tile" style="--color: #93B2E9">
                <header>Generation</header>
            <div class="box-content">
                        <div class="content">
                            <h3 class="title">For example</h3>
                            <span class="post">Image</span>
                            <span class="post">Creative Board</span>
                            <span class="post">Voice</span>
                        </div>
                    </div>
            </div>
            <div class="type4 tile" style="--color: #92E6D1">
                <header>Others</header>
             <div class="box-content">
                        <div class="content">
                            <h3 class="title">For example</h3>
                            <span class="post">Text Translate</span>
                        </div>
                    </div>
            </div>
        </div>
    </div>
    <!-- <div class="mouser"></div> -->
        <div class="copyrigntoutbox"><span class="copyrigntmsg">Copyright © 2020 Northwestern Polytechnical University All Rights Reserved</span></div>
    </div>
</template>
<script>
import '@/assets/css/style.css';
import '@/assets/css/normalize.min.css';
import '@/assets/js/index.js.下载';
import '@/assets/css/Datacages_Homeindex.css';
export default {
    data: function () {
        return {
            param: {
                username: 'admin',
                password: '123456'
            }
            // rules: {
            //     username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
            //     password: [{ required: true, message: '请输入密码', trigger: 'blur' }]
            // }
        };
    },
    methods: {
        gotoIdentification() {
            this.$router.push('/identificationtaskplus');
        },
    },
    mounted() {
        window.onload = function () {
            var loading = document.getElementById('loading');
            loading.style.display = 'none';
        };
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
            overflow-y:hidden;
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
         .tile:hover .content  {
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
</style>