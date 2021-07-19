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
                    style="height: 620px; padding: 5px; background-color: rgba(0, 168, 255, 0.2); border: 0"
                    :body-style="{ padding: '0px' }"
                >
                    <div class="header-box1">
                        <img src="../../assets/img/result.png" style="width: 60px; height: 45px" />
                        <span class="header-name">Computing Results</span>
                    </div>
                    <div class="divider div-transparent"></div>
                    <!-- <video src="../../assets/img/tokyo-street.mp4" controls="controls" class="video"></video> -->
                    <div class="next-btn" @click="taskmode()">
                        <a class="flowbutton"><span></span><span></span><span></span><span></span>Download</a>
                    </div>
                    <div class="digital">
                        <table width="100%" id="userImportTable" border="0" cellpadding="0" cellspacing="0">
                            <thead>
                                <tr>
                                    <th>Frame</th>
                                    <th>Upper Left Corner</th>
                                    <th>Lower Right Corner</th>
                                    <th>Confidence</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>c4s3_008073</td>
                                    <td>(10,25)</td>
                                    <td>(302,430)</td>
                                    <td>0.95</td>
                                </tr>
                                <tr>
                                    <td>c4s3_008094</td>
                                    <td>(630,230)</td>
                                    <td>(1036,788)</td>
                                    <td>0.94</td>
                                </tr>
                                <tr>
                                    <td>c4s3_008123</td>
                                    <td>(462,387)</td>
                                    <td>(898,846)</td>
                                    <td>0.96</td>
                                </tr>
                                <tr>
                                    <td>c4s3_008158</td>
                                    <td>(103,158)</td>
                                    <td>(758,649)</td>
                                    <td>0.98</td>
                                </tr>
                            </tbody>
                        </table>

                        <div class="userImportTableBottom">
                            <div class="tablePageinate">
                                <a
                                    class="pageinateBtn previous"
                                    aria-controls="userImportTable"
                                    pageid="2"
                                    tabindex="0"
                                    previouspage="0"
                                    id="pagePrevious"
                                    >&lt;</a
                                ><span class="pageBtnS"
                                    ><a
                                        class="pageinateBtn"
                                        aria-controls="userImportTable"
                                        pageid="1"
                                        tabindex="0"
                                        style="display: inline-block"
                                        >1</a
                                    ><a
                                        class="pageinateBtn"
                                        aria-controls="userImportTable"
                                        pageid="2"
                                        tabindex="0"
                                        style="display: inline-block"
                                        >2<!-- a--></a
                                    ><a
                                        class="pageinateBtn current"
                                        aria-controls="userImportTable"
                                        pageid="3"
                                        tabindex="0"
                                        style="display: inline-block"
                                        >3<!-- a--></a
                                    ></span
                                ><a
                                    class="pageinateBtn next"
                                    aria-controls="userImportTable"
                                    pageid="4"
                                    tabindex="0"
                                    nextpage="3"
                                    id="pageNext"
                                    >&gt;</a
                                >
                            </div>
                            <div class="clearBoth"></div>
                        </div>
                    </div>
                    <!-- <el-table :data="tableData"   :header-cell-style="{background:black,borderColor:'#CECECE',textAlign:'center'}" style="width: 100%">
                        <el-table-column prop="date" label="Frame" > </el-table-column>
                        <el-table-column prop="name" label="Upper Left Corner"> </el-table-column>
                        <el-table-column prop="address" label="Lower Right Corner"> </el-table-column>
                        <el-table-column prop="conf" label="Confidence"> </el-table-column>
                    </el-table> -->
                </el-card>
            </el-col>
            <el-col :span="8">
                <el-card
                    shadow="hover"
                    style="height: 620px; padding: 5px; background-color: rgba(0, 168, 255, 0.2); border: 0"
                    :body-style="{ padding: '0px' }"
                >
                    <div class="header-box1">
                        <img src="../../assets/img/detail.png" style="width: 45px; height: 45px" />
                        <span class="header-name">Computing Details</span>
                    </div>
                    <div class="divider div-transparent"></div>
                                                <div class="table-responsive">
                                <table class="table table-bordered">
                                    <tbody>
                                        <tr>
                                            <th scope="row">Human used:</th>
                                            <td>5*Expert</td>
                                        </tr>
                                        <tr>
                                            <th scope="row">Machine used:</th>
                                            <td>5*RTX TITAN</td>
                                        </tr>
                                        <tr>
                                            <th scope="row">Computing mode:</th>
                                            <td>Parallel computing</td>
                                        </tr>
                                        <tr>
                                            <th scope="row">Collaboration mode:</th>
                                            <td>Verification</td>
                                        </tr>
                                        <tr>
                                            <th scope="row">Storage occupancy:</th>
                                            <td>20G</td>
                                        </tr>
                                        <tr>
                                            <th scope="row">Start time:</th>
                                            <td>2020/11/1 10:00</td>
                                        </tr>
                                       <tr>
                                            <th scope="row">Task execution time:</th>
                                            <td>6hour 30min</td>
                                        </tr>
                                        <tr>
                                            <th scope="row">Accuracy:</th>
                                            <td>94.0%</td>
                                        </tr>
                                        <tr>
                                            <th scope="row">Number of iterations:</th>
                                            <td>5 times</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                     <div class="next-btn1" @click="taskmode()">
                        <a class="flowbutton"><span></span><span></span><span></span><span></span>accept</a>
                    </div>
                   <div class="next-btn2" @click="taskmode()">
                        <a class="flowbutton"><span></span><span></span><span></span><span></span>iterate</a>
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
            tableData: [
                {
                    date: 'c4s3_008073',
                    name: '(10,25)',
                    address: '(302,430)',
                    conf: '0.95'
                },
                {
                    date: 'c4s3_008094',
                    name: '(630,230)',
                    address: '(1036,788)',
                    conf: '0.94'
                },
                {
                    date: 'c4s3_008123',
                    name: '(462,387)',
                    address: '(898,846)',
                    conf: '0.96'
                },
                {
                    date: 'c4s3_008158',
                    name: '(103,158)',
                    address: '(758,649)',
                    conf: '0.98'
                }
            ],
            //  url: { url: require('../../assets/img/work.gif') },
            url: { url: require('../../assets/img/work.png') },
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
    computed: {
        role() {
            return this.name === 'admin' ? '超级管理员' : '普通用户';
        }
    },

    methods: {
        taskmode() {
            this.$router.push('/taskmodeplus');
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
        // 调用时机根据需求
        this.countTime(this.start_time);
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

.user-info-cont div:first-child {
    font-size: 30px;
    color: #222;
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
.next-btn {
    float: right;
    width: 100px;
    height: 40px;
    line-height: 40px;
    padding: 0 25px;
    margin-top: 130px;
    font-size: 14px;
    margin-right: 90px;
    border-radius: 4px;
    box-sizing: border-box;
    cursor: pointer;
}
.next-btn1 {
    float: right;
    width: 100px;
    height: 40px;
    line-height: 40px;
    padding: 0 25px;
    font-size: 14px;
    margin-right: 80px;
    border-radius: 4px;
    box-sizing: border-box;
    cursor: pointer;
}
.next-btn2 {
    float: right;
    width: 100px;
    height: 40px;
    line-height: 40px;
    padding: 0 25px;
    font-size: 14px;
    margin-right: 90px;
    border-radius: 4px;
    box-sizing: border-box;
    cursor: pointer;
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
    letter-spacing: 0px;
    font-size: 24px;
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

canvas {
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    pointer-events: none;
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
.video {
    margin-left: 150px;
    width: 495px;
    height: 300px;
}
	.digital{
				width: 85%;
				margin: 0px auto;
			}
			.digitalTitle{
			    height: 60px;
    			line-height: 60px;
			    font-size: 16px;
			}
			.CAButtonS{
				margin: 10px 0;
			}

			table.dataTable tbody tr,.reseachIput,#tablesLength>label>select,#tablesPageinate .pageinateBtn{
			    background: #03152E;
			}
			.requestBtn{
				vertical-align: baseline;
				margin-left: 16px;
			}
			#userImportTable{
			    background: #003975;
			    color: #fff;
			    border: none!important;
			    text-align: center;
			    margin: 5px 0;
			}
			#userImportTable tr{
				height: 40px;
				line-height: 40px;
			}
			/*自定义表格格式*/
			table tbody tr, .reseachIput, #tablesLength>label>select, #tablesPageinate .pageinateBtn{
				background: #03152E;
			}
			.reseachIputCertificate{
			    height: 40px;
			    width: 500px;
			    background: #03152E;

			    border-radius: 4px;
			    border: none;
			    padding: 0 6px;
			    color: #fff;
			}
			.uploadDigital{
				/*border: 1px solid red;*/
			}
			.uploadDigitalLabel{
			    /*width: 510px;*/
    			float: right;
				
			}
			
			.uploadDigitalInput{
				width: 300px;
			    background: #03152E;
			    border: none;
			    height: 40px;
			    border-radius: 4px;
			    color: #fff;
			    padding:0 6px;
			    margin-right: 16px;
    			vertical-align: middle;
			}
			.digitalTop{
				margin-bottom: 7px;
			}
			.userImportTableBottom{
				/*color: #fff;*/
			}
			.userImportTableBottom .dataTablesInfo{
				float: left;
			}
			.userImportTableBottom  .tablePageinate,.userImportTableBottom  .digitalLength{
				float: right;
			}
			.userImportTableBottom  .digitalLength{
				float: right;
			    padding-top: 0.25em;
			    margin-right: 20px;
			}
			.userImportTableBottom  .digitalLength select{
				background: #03152E;
			    border: none;
			    border-radius: 4px;
			    color: #fff;
			    margin: 0 4px;
			    padding: 4px;
			}
			.tablePageinate .pageinateBtn.current{
			    width: 30px;
			    height: 30px;
			    font-size: 12px;
			    background: #03e9f4;
			    text-align: center;
			    line-height: 30px;
			    border-radius: 4px;
			    color: #fff!important;
			    border: none!important;
			}
			#pageNext:hover,#pagePrevious:hover,.tablePageinate .pageinateBtn:hover {
		    	background: #03e9f4;
		    	cursor: pointer;
		    }
		    .tablePageinate .disabled{
		    	cursor: no-drop!important;
		    }
			#pageNext,#pagePrevious,.tablePageinate .pageinateBtn {
				display: inline-block;
				width: 30px;
			    height: 30px;
			    margin: 0px 2px;
			    font-size: 12px;
			    background: #03152E;
			    text-align: center;
			    line-height: 30px;
			    border-radius: 4px;
			    color: #fff!important;
			    border: none!important;
			}
			.userImportTableBottom .dataTablesInfo>button{
				color: #fff;
			    margin-left: 20px;
			}
			.clearBoth{
				clear: both;
			}
			.selectedNumDigital{
				color: #0589E0;
    			margin: 0 2px;
			}
			.importBtns{
				text-align: center;
				margin-top: 20px;
			}
			.importBtns>button{
		    	height: 38px;
				line-height: 38px;
    			border: none;
    			color: #fff;
    			margin: 0 6px;
			}
			.roleSlect{
			    background: #03152E;
			    padding: 4px 6px;
			    border: none;
			    color: #fff;
			}
			.reminder{
			    font-size: 13px;
			    text-align: center;
			    background: #03152E;
			    height: 40px;
			    color: #fff;
			    margin-top: -20px;
			    margin-bottom: 20px;
			    line-height: 40px;
			}
			/*.showDatas{
				text-align: center;
			}*/
			.showDatasBtn,.checkBtn{
				background: #0589E0;
   				border: none;
			    color: #fff;
			    padding: 4px 6px ;
			    border-radius: 4px;
			    cursor: pointer;
			    opacity: 0.8;
			}
			button:hover{
			    opacity: 1;
			}
            .table-bordered {
    border: 1px solid #dee2e6
}

.table-bordered td,
.table-bordered th {
    border: 1px solid #dee2e6
}
.table-bordered tr{
    /* background: transparent; */
    background:#03152E;
}
.table-bordered th{
    color: white;
}
.table-bordered td{
       background:rgba(0, 168, 255, 0.2);
     color: #03e9f4;
     font-weight: 400;
}

.table-bordered thead td,
.table-bordered thead th {
    border-bottom-width: 2px
}
</style>