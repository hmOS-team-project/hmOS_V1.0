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
            <el-col :span="17">
                <el-card
                    shadow="hover"
                    style="height: 640px; padding: 5px; background-color: rgba(0, 168, 255, 0.2); border: 0"
                    :body-style="{ padding: '0px' }"
                >
                    <div class="header-box1">
                        <img src="../../assets/img/hmmode.png" style="width: 45px; height: 45px" />
                        <span class="header-name">Mode Select</span>
                    </div>
                    <div class="divider div-transparent"></div>
                    <div class="w_box clearfix sp_page2_area">
                        <div class="button-box">
                            <el-radio v-model="radio" :label="true">Default</el-radio>
                            <el-radio v-model="radio" :label="false">User Defined</el-radio>
                        </div>
                        <div class="sp_page2">
                            <ul class="timePointAreaSp">
                                <li class="time_point_list">
                                    <div class="txt_area" style="margin-top: 30px">
                                        <div class="tips_area">
                                            <div class="tasktype-box">
                                                <!-- <el-tooltip class="item" effect="light" content="任务执行前，包括数据标注、数据预处理例如视频段选择和异常数据处理等" placement="top">
                            <div class="tasktype1-header">创建协作</div>
                              </el-tooltip> -->
                                                <div class="tasktype1">
                                                    <el-tooltip class="item" effect="light" content="分发（快速完成）" placement="top">
                                                        <img
                                                            src="../../assets/img/mode3.png"
                                                            style="width: 500px; height: 100px"
                                                            HorizontalAlignment="Left"
                                                        />
                                                    </el-tooltip>
                                                    <div class="div-choose">
                                                        <el-radio v-model="createMode" label="1" :disabled="radio">{{ '' }}</el-radio>
                                                    </div>
                                                </div>
                                                <div class="tasktype1">
                                                    <el-tooltip class="item" effect="light" content="择优（高精度要求）" placement="top">
                                                        <img src="../../assets/img/mode4.png" style="width: 500px; height: 100px" />
                                                    </el-tooltip>
                                                    <div class="div-choose">
                                                        <el-radio v-model="createMode" label="2" :disabled="radio">{{ '' }}</el-radio>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="content_area">
                                            <div class="time_point timePoint" style="margin-left: 15px">
                                                <span
                                                    style="
                                                        font-size: 18px;
                                                        color: #03e9f4;
                                                        margin-right: 18px;
                                                        font-weight: 400;
                                                        text-align: center;
                                                    "
                                                    >Create</span
                                                >
                                                <em class="point1"></em>
                                                <em class="light"></em>
                                            </div>
                                        </div>
                                    </div>
                                </li>
                                <li class="time_point_list active">
                                    <div class="txt_area">
                                        <div class="tips_area">
                                            <div class="tasktype-box">
                                                <!-- <el-tooltip class="item" effect="light" content="任务执行前，包括数据标注、数据预处理例如视频段选择和异常数据处理等" placement="top">
                            <div class="tasktype1-header">创建协作</div>
                              </el-tooltip> -->
                                                <div class="tasktype2">
                                                    <el-tooltip class="item" effect="light" content="分发（快速完成）" placement="top">
                                                        <img
                                                            src="../../assets/img/mode1.png"
                                                            style="width: 500px; height: 100px"
                                                            HorizontalAlignment="Left"
                                                        />
                                                    </el-tooltip>
                                                    <div class="div-choose">
                                                        <el-radio v-model="executionMode" label="1" :disabled="radio">{{ '' }}</el-radio>
                                                    </div>
                                                </div>
                                                <div class="tasktype2">
                                                    <el-tooltip class="item" effect="light" content="择优（高精度要求）" placement="top">
                                                        <img src="../../assets/img/mode2.png" style="width: 500px; height: 100px" />
                                                    </el-tooltip>
                                                    <div class="div-choose">
                                                        <el-radio v-model="executionMode" label="2" :disabled="radio">{{ '' }}</el-radio>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="content_area">
                                            <div class="time_point timePoint">
                                                <span style="font-size: 18px; color: #03e9f4; margin-right: 33px; font-weight: 400">
                                                    Execution</span
                                                >
                                                <em class="point1"></em>
                                                <em class="light"></em>
                                            </div>
                                        </div>
                                    </div>
                                </li>
                                <li class="time_point_list">
                                    <div class="txt_area">
                                        <div class="tips_area">
                                            <div class="tasktype-box">
                                                <!-- <el-tooltip class="item" effect="light" content="任务执行前，包括数据标注、数据预处理例如视频段选择和异常数据处理等" placement="top">
                            <div class="tasktype1-header">创建协作</div>
                              </el-tooltip> -->
                                                <div class="tasktype3">
                                                    <el-tooltip class="item" effect="light" content="分发（快速完成）" placement="top">
                                                        <img
                                                            src="../../assets/img/mode5.png"
                                                            style="width: 500px; height: 100px"
                                                            HorizontalAlignment="Left"
                                                        />
                                                    </el-tooltip>
                                                    <div class="div-choose">
                                                        <el-radio v-model="verificationMode" label="1" :disabled="radio">{{ '' }}</el-radio>
                                                    </div>
                                                </div>
                                                <div class="tasktype3">
                                                    <el-tooltip class="item" effect="light" content="择优（高精度要求）" placement="top">
                                                        <img src="../../assets/img/mode6.png" style="width: 500px; height: 100px" />
                                                    </el-tooltip>
                                                    <div class="div-choose">
                                                        <el-radio v-model="verificationMode" label="2" :disabled="radio">{{ '' }}</el-radio>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="content_area">
                                            <div class="time_point timePoint">
                                                <span style="font-size: 18px; color: #03e9f4; margin-right: 33px; font-weight: 400"
                                                    >Verification</span
                                                >
                                                <em class="point1"></em>
                                                <em class="light"></em>
                                            </div>
                                        </div>
                                    </div>
                                </li>
                            </ul>
                        </div>
                        <div class="next-btn1" @click="laststep()">
                            <a class="flowbutton"><span></span><span></span><span></span><span></span>back</a>
                        </div>

                        <div class="next-btn2" @click="submittask()">
                            <a class="flowbutton"><span></span><span></span><span></span><span></span>Submit</a>
                        </div>
                    </div>
                </el-card>
                <div class="copyrigntoutbox" style="position: relative; top: 0px">
                    <span class="copyrigntmsg">Copyright © 2020 Northwestern Polytechnical University All Rights Reserved</span>
                </div>
            </el-col>
            <el-col :span="7">
                <el-card
                    shadow="hover"
                    style="height: 640px; padding: 5px; background-color: rgba(0, 168, 255, 0.2); border: 0"
                    :body-style="{ padding: '0px' }"
                >
                    <div class="header-box1">
                        <img src="../../assets/img/dataset.png" style="width: 50px; height: 45px" />
                        <span class="header-name">Dataset</span>
                    </div>
                    <div class="divider div-transparent"></div>
                    <el-col :span="24">
                        <div style="font-size: 22px; color: rgb(3, 233, 244); font-weight: 400; margin-left: 20px">Choose the target</div>
                        <div class="crop-demo">
                            <img :src="cropImg" class="pre-img" />
                            <div class="crop-btn-box">
                                <div class="upload-btn">
                                    <a class="flowbutton"
                                        ><span></span><span></span><span></span><span></span>
                                        <input class="crop-input" @click="uploadQuery()" />
                                        upload</a
                                    >
                                </div>
                                <div class="next-btn">
                                    <a class="flowbutton"
                                        ><span></span><span></span><span></span><span></span>
                                        <input class="crop-input" type="file" name="image" accept="image/*" @change="setImage" />
                                        Select</a
                                    >
                                </div>
                            </div>
                        </div>
                        <div style="font-size: 22px; color: rgb(3, 233, 244); font-weight: 400; margin-left: 20px; margin-top: 65px">
                            Upload the dataset
                        </div>
                        <el-upload
                            class="upload-demo"
                            action
                            :http-request="Upload"
                            :before-upload="beforeAvatarUpload"
                            :on-preview="handlePreview"
                            :before-remove="beforeRemove"
                            :on-remove="handleRemove"
                            :on-success="handleSuccess"
                            :on-exceed="handleExceed"
                            drag
                            :limit="limit"
                            :file-list="fileList"
                        >
                            <i class="el-icon-upload"></i>
                            <div class="el-upload__text">Drag the video or text to be detected here,or <em>click here</em></div>
                        </el-upload>
                        <el-progress v-show="showProgress" :text-inside="true" :stroke-width="15" :percentage="progress"></el-progress>
                        <div style="margin-top: 40px">
                            <div class="next-btn3" @click="submitdataset()">
                                <a class="flowbutton"><span></span><span></span><span></span><span></span>Finished</a>
                            </div>
                        </div>
                        <el-dialog title="裁剪图片" :visible.sync="dialogVisible" width="30%">
                            <vue-cropper
                                ref="cropper"
                                :src="imgSrc"
                                :ready="cropImage"
                                :zoom="cropImage"
                                :cropmove="cropImage"
                                style="width: 100%; height: 300px"
                            ></vue-cropper>
                            <span slot="footer" class="dialog-footer">
                                <el-button @click="cancelCrop">取 消</el-button>
                                <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
                            </span>
                        </el-dialog>
                    </el-col>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>
<script>
import '@/assets/css/style.css';
import '@/assets/css/normalize.min.css';
import '@/assets/js/index.js.下载';
import '@/assets/js/timejquery.js.下载';
import '@/assets/css/Datacages_Homeindex.css';
import identificationtaskplus from './IdentificationTaskPlus';
import VueCropper from 'vue-cropperjs';
import { client, getFileNameUUID } from '@/utils/ali-oss';
export default {
    components: {
        identificationtaskplus,
        VueCropper
    },
    props: {
        limit: {
            type: Number,
            default: 1
        }
    },
    data: function () {
        return {
            defaultSrc: require('../../assets/img/person.jpg'),
            taskId: '',
            // cropImg: require('../../assets/img/person.jpg'),
            imgSrc: '',
            cropImg: '',
            dialogVisible: false,
            radio: true,
            createMode: '1',
            executionMode: '1',
            verificationMode: '1',
            fileList: [], //文件列
            showProgress: false, //进度条的显示
            dataObj: {}, //存签名信息
            progress: 0 //进度条数据
        };
    },
    methods: {
        laststep() {
            this.$router.push('/identificationtaskplus');
        },
        submittask() {
            this.$confirm('This operation will submit the task. Do you want to continue?', 'Tips', {
                confirmButtonText: 'Submit',
                cancelButtonText: 'Cancel',
                type: 'warning'
            })
                .then(() => {
                    let input = JSON.parse(decodeURIComponent(this.$route.params.input));
                    let time = new Date();
                    let y = time.getFullYear();
                    let m = time.getMonth() + 1;
                    let d = time.getDate();
                    let H = time.getHours();
                    let min = time.getMinutes();
                    let myDate = y + '-' + m + '-' + d + '-' + H + ':' + min;
                    let data = {
                        taskName: input.taskName,
                        taskTimeRequire: input.taskTimeRequire,
                        taskAccRequire: input.taskAccRequire,
                        taskStatus: 'Unexecuted',
                        taskType: 'Identification',
                        description: input.description,
                        startTime: myDate,
                        resourceIsCustom: input.resourceIsCustom,
                        modelIsCustom: input.modelIsCustom,
                        queryUrl: '',
                        videoUrl: '',
                        resultUrl: ''
                    };
                    this.$axios.post('http://localhost:3000/api/task/createtask', data).then((res) => {
                        if (res.data.success) {
                            this.taskId = res.data.taskId;
                            this.$message({
                                type: 'success',
                                message: 'Submitted successfully!'
                            });
                        } else {
                            alert('Submitted failed！');
                        }
                    });
                })
                .catch(() => {
                    this.$message({
                        type: 'info',
                        message: 'Submission canceled'
                    });
                });
        },
        uploadQuery() {
            let file = document.getElementsByName('image')[0].files[0];
            let formData = new FormData();
            if (file == undefined) {
                alert('please select a query!');
            } else if (this.taskId == '') {
                alert('please submit task information first!');
            } else {
                formData.append('file', file, this.taskId + '-' + file.name);
                this.$axios
                    .post('http://localhost:2333/upload/single', formData, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    })
                    .then((res) => {
                        if (res.data.code === '200') {
                            let data = {
                                queryUrl: res.data.originalname,
                                taskId: this.taskId
                            };
                            this.$axios.post('http://localhost:3000/api/task/queryUrl', data).then((res) => {
                                if (res.data.success) {
                                    this.$message({
                                        type: 'success',
                                        message: 'Submitted successfully!'
                                    });
                                } else {
                                    alert('Submitted failed！');
                                }
                            });
                        } else {
                            alert('upload failed');
                        }
                    })
                    .catch((err) => {
                        console.log(err);
                    });
            }
        },
        setImage(e) {
            const file = e.target.files[0];
            if (!file.type.includes('image/')) {
                return;
            }
            const reader = new FileReader();
            reader.onload = (event) => {
                this.dialogVisible = true;
                this.imgSrc = event.target.result;
                this.$refs.cropper && this.$refs.cropper.replace(event.target.result);
            };
            reader.readAsDataURL(file);
        },
        cropImage() {
            this.cropImg = this.$refs.cropper.getCroppedCanvas().toDataURL();
        },
        cancelCrop() {
            this.dialogVisible = false;
            this.cropImg = this.defaultSrc;
        },
        // 文件超出个数限制时的钩子
        handleExceed(files, fileList) {
            this.$message.warning(`每次只能上传 ${this.limit} 个文件`);
        },
        // 点击文件列表中已上传的文件时的钩子
        handlePreview(file) {},
        // 删除文件之前的钩子
        beforeRemove(file, fileList) {
            return this.$confirm(`确定移除 ${file.name}？`);
        },
        // 文件列表移除文件时的钩子
        handleRemove(file, fileList) {},
        // 文件上传成功时的钩子
        handleSuccess(response, file, fileList) {
            this.fileList = fileList;
        },
        //文件上传前的校验
        beforeAvatarUpload(file) {
            const isLt100M = file.size / 1024 / 1024 / 10 < 1024;
            const isLt30 = file.name.length < 30;
            //   if (["video/mp4"].indexOf(file.type) == -1) {
            //     this.$message.error("请上传正确的视频格式");
            //     return false;
            //   }
            if (!isLt100M) {
                this.$message.error('上传视频大小要在10MB~1GB之间哦!');
                return false;
            }
            if (!isLt30) {
                this.$message.error('上传视频文件名称长度必须要小于30个文字哦!');
                return false;
            }
        },
        // http-request属性来覆盖默认的上传行为（即action="url"），自定义上传的实现
        Upload(file) {
            const that = this;
            if (that.taskId == '') {
                alert('please submit task information first!');
            } else {
                async function multipartUpload() {
                    let temporary = file.file.name.lastIndexOf('.');
                    let fileNameLength = file.file.name.length;
                    let fileFormat = file.file.name.substring(temporary + 1, fileNameLength);
                    let fileName = that.taskId + '-' + getFileNameUUID() + '.' + fileFormat;
                    client()
                        .multipartUpload(`Dataset/${fileName}`, file.file, {
                            progress: function (p) {
                                //p进度条的值
                                console.log(p);
                                that.showProgress = true;
                                that.progress = Math.floor(p * 100);
                            }
                        })
                        .then((result) => {
                            let  temp = result.name.split('/');
                           // 上传成功返回值，可针对项目需求写其他逻辑
                            let data = {
                                videoUrl: temp[1],
                                taskId: that.taskId
                            };
                            that.$axios.post('http://localhost:3000/api/task/videoUrl', data).then((res) => {
                                if (res.data.success) {
                                    that.$message({
                                        type: 'success',
                                        message: 'Submitted successfully!'
                                    });
                                } else {
                                    alert('Submitted failed！');
                                }
                            });
                        })
                        .catch((err) => {
                            console.log('err:', err);
                        });
                }
                multipartUpload();
            }
        },

        submitdataset() {
            this.$message({
                type: 'success',
                message: 'Submitted successfully!'
            });
            this.$router.push('/homeplus');
        }
    },
    mounted() {
        window.onload = function () {
            var loading = document.getElementById('loading');
            loading.style.display = 'none';
        };
        $(function () {
            $('.timePointAreaSp .timePoint').click(function () {
                $(this).parents('.time_point_list').addClass('active').siblings().removeClass('active');
            });
        });
    },
    created() {
        this.cropImg = this.defaultSrc;
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
.w_box {
    width: 96%;
    max-width: 810px;
    margin-left: 60px;
}

.clearfix:after {
    content: '.';
    display: block;
    height: 0;
    clear: both;
    visibility: hidden;
}

.clearfix {
    *+height: 1%;
}

.disabled {
    cursor: not-allowed;
}

.img {
    position: relative;
}

.img em {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    -webkit-transition: all 0.3s ease-out;
    transition: all 0.3s ease-out;
    cursor: pointer;
}

.sp_page2 .time_point_list {
    list-style-type: none;
    position: relative;
    padding-top: 80px;
}

.sp_page2 .time_point_list.active {
    padding: 0;
}

.sp_page2 .time_point_list.active:before,
.sp_page2 .time_point_list.active:after {
    background-image: none;
}

.sp_page2 .time_point_list:last-child {
    padding-bottom: 100px;
}

.sp_page2 .time_point_list:last-child.active {
    /* padding-bottom: 130px; */
}

.sp_page2 .time_point_list em {
    display: inline-block;
    width: 35px;
    height: 35px;
    vertical-align: middle;
    background-size: contain;
}

.sp_page2 .time_point_list em.light,
.sp_page2 .time_point_list.active em {
    display: none;
}

.sp_page2 .time_point_list.active em.light {
    background-image: url(../../assets/img/sp_page2_point2.png);
    display: inline-block;
}

.sp_page2 .txt_area {
    position: relative;
    display: inline-block;
    width: calc(100% - 150px);
    margin-left: 150px;
    font-size: 14px;
    color: #fff;
    line-height: 1.8;
    text-align: center;
}

.sp_page2 .tips_area {
    padding: 2px 5px;
    margin-bottom: 10px;
    border-radius: 4px;
    background: rgba(0, 168, 255, 0.2);
    border: 1px solid rgba(255, 255, 255, 0.3);
}

.sp_page2 .txt_area:after {
    position: absolute;
    bottom: -6px;
    left: -60px;
    width: 20px;
    height: calc(90% + 14px);
    content: '';
    background: url(../../assets/img/sp_page2_solid3.png) no-repeat center top;
    background-size: contain;
}

.sp_page2 .desc_area {
    font-size: 15px;
    line-height: 1.8;
    width: 96%;
}

.sp_page2 .content_area {
    position: relative;
}

.sp_page2 .content_area .content {
    padding: 10px;
    margin-bottom: 15px;
    background: rgba(22, 48, 110, 0.4);
    border: 1px solid rgba(255, 255, 255, 0.3);
}

.sp_page2 .content_area .time_point {
    position: absolute;
    left: -160px;
    bottom: -5px;
    line-height: 35px;
    z-index: 2;
    cursor: pointer;
}

.sp_page2 .time_point span {
    display: inline-block;
    width: 60px;
}

.sp_page2 .content_area h3 {
    font-size: 16px;
    color: #2ea9fc;
    margin-bottom: 10px;
}

.sp_page2 .version_area {
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
}

.sp_page2 .rang_version {
    border-radius: 40px;
    padding: 5px;
    margin-bottom: 10px;
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.3);
}

.sp_page2 .rang_content {
    color: #e88700;
}

.sp_page2 .rang_content strong {
    font-size: 18px;
    color: #fff;
    font-weight: normal;
}

.sp_page2 .tips_area,
.sp_page2 .content_area .content,
.sp_page2 .rang_version,
.sp_page2 .rang_content {
    display: none;
}

.sp_page2 .time_point_list.active .tips_area,
.sp_page2 .time_point_list.active .content_area .content,
.sp_page2 .time_point_list.active .rang_version,
.sp_page2 .time_point_list.active .rang_content {
    display: block;
}

.sp_page2 .time_point_list.active .content_area:after {
    position: absolute;
    bottom: 0px;
    left: -55px;
    width: 55px;
    height: 13px;
    content: '';
    background: url(../../assets/img/sp_page2_solid1.png) no-repeat center top;
    background-size: contain;
}

.sp_page2 .time_point_list:before {
    position: absolute;
    top: 3px;
    left: 90px;
    width: 20px;
    height: 63px;
    content: '';
    background: url(../../assets/img/sp_page2_solid3.png) no-repeat center top;
    background-size: contain;
}

.sp_page2 .time_point_list:after {
    position: absolute;
    bottom: 0;
    left: 90px;
    width: 20px;
    height: 0;
    content: '';
}

.sp_page2 .time_point_list:first-child:before {
    background: url(../../assets/img/sp_page2_solid2.png) top center;
}

.sp_page2 .time_point_list.active:first-child .txt_area:after {
    background-image: url(../../assets/img/sp_page2_solid2.png);
}

.sp_page2 .time_point_list.active:first-child:before {
    background-image: none;
}

.sp_page2 .time_point_list:last-child:after {
    height: 115px;
    bottom: -46px;
    background: url(../../assets/img/sp_page2_solid4.png) bottom center no-repeat;
}

.sp_page2 .time_point_list:last-child.active:after {
    bottom: 0;
}

.sp_page2 .time_point_list.active + .time_point_list:before {
    top: -5px;
    height: 40px;
}
.point1 {
    background-image: url(../../assets/img/sp_page2_point1.png);
}
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
.grid-content {
    display: flex;
    align-items: center;
    height: 40px;
}

.grid-cont-right {
    flex: 1;
    text-align: center;
    font-size: 14px;
    color: #999;
}

.grid-num {
    font-size: 24px;
    font-weight: bold;
}

.grid-con-icon {
    font-size: 24px;
    width: 40px;
    height: 40px;
    text-align: center;
    line-height: 40px;
    color: #fff;
}

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
}
.crop-demo {
    margin-left: 80px;
    margin-top: 40px;
    margin-bottom: 40px;
    width: 260px;
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
.crop-input {
    position: absolute;
    width: 130px;
    height: 40px;
    left: 0;
    top: 0;
    opacity: 0;
}
.upload-demo {
    width: 300px;
    margin-top: 40px;
    margin-left: 13px;
}
.query_input {
    margin-left: 360px;
}
.crop-btn-box {
    margin-top: 18px;
}

.task-submit-box {
    margin-left: 150px;
}
.tasktype1-header {
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    background: rgba(0, 168, 255, 0.2);
    text-align: center;
    height: 120px;
    width: 40px;
    margin: 10px;
}
.tasktype2-header {
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    background: rgba(0, 168, 255, 0.2);
    text-align: center;
    height: 120px;
    width: 40px;
    margin: 10px;
}
.tasktype3-header {
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    background: rgba(0, 168, 255, 0.2);
    text-align: center;
    height: 120px;
    width: 40px;
    margin: 10px;
}
.tasktype1 {
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    background: rgba(0, 168, 255, 0.2);
    text-align: center;
    height: 120px;
    width: 600px;
    margin: 10px;
}
.tasktype2 {
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    background: rgba(0, 168, 255, 0.2);
    text-align: center;
    height: 120px;
    width: 600px;
    margin: 10px;
}
.tasktype3 {
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    background: rgba(0, 168, 255, 0.2);
    text-align: center;
    height: 120px;
    width: 600px;
    margin: 10px;
}
.tasktype-name {
    font-size: 22px;
    font-weight: 800;
}
.typeinformation-title {
    font-size: 22px;
    font-weight: 800;
    margin-left: 10px;
}
.typeinformation-header {
    display: flex;
    align-items: center;
}
.typeinformation-name-box {
    display: flex;
    align-items: center;
}
.typeinformation-name1 {
    text-align: center;
    width: 95px;
    margin: 25px 15px 25px 15px;
    background-color: #ffb5c5;
    font-size: 18px;
    cursor: pointer;
}
.typeinformation-name2 {
    text-align: center;
    width: 95px;
    margin: 25px 15px 25px 15px;
    background-color: #aeeeee;
    font-size: 18px;
    cursor: pointer;
}
.typeinformation-name3 {
    text-align: center;
    width: 95px;
    margin: 25px 15px 25px 15px;
    background-color: #9aff9a;
    font-size: 18px;
    cursor: pointer;
}
.typeinformation-name4 {
    text-align: center;
    width: 95px;
    margin: 25px 15px 25px 15px;
    background-color: #bebebe;
    font-size: 18px;
    cursor: pointer;
}
.header-box2 {
    width: 200px;
    height: 50px;
    background: url('../../assets/img/icon-typebackground.png') no-repeat;
    background-size: 100% 100%;
    display: flex;
    align-items: center;
}
.typeinformation-cont {
    padding: 15px;
}
.tasktype-box {
    display: flex;
    flex-wrap: wrap;
    margin-left: 20px;
}
.div-header {
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    height: 10px;
    margin-left: 30px;
    width: 40px;
}
.submit-btn {
    position: relative;
    width: 100px;
    height: 40px;
    line-height: 40px;
    padding: 0 33px;
    margin: 5px;
    background-color: #409eff;
    color: #fff;
    font-size: 14px;
    border-radius: 4px;
    box-sizing: border-box;
    cursor: pointer;
}
.button-box {
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    left: 45%;
    z-index: 5;
}
.div-choose {
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    height: 40px;
    margin-left: 25px;
}
.el-radio >>> .el-radio__inner {
    border-color: #03e9f4;
}
.el-radio >>> .el-radio__label {
    color: #03e9f4;
}
.next-btn {
    position: relative;
    width: 100px;
    height: 40px;
    line-height: 40px;
    padding: 0 25px;
    margin-left: 100px;
    margin-top: -100px;
    font-size: 14px;
    border-radius: 4px;
    box-sizing: border-box;
    cursor: pointer;
}
.upload-btn {
    position: relative;
    width: 100px;
    height: 40px;
    line-height: 40px;
    padding: 0 25px;
    margin-left: 90px;
    margin-top: -65px;
    font-size: 12px;
    border-radius: 4px;
    box-sizing: border-box;
    cursor: pointer;
}
.next-btn1 {
    position: absolute;
    width: 80px;
    height: 40px;
    line-height: 40px;
    padding: 0 25px;
    top: 500px;
    margin-left: 270px;
    /* margin-top: -65px; */
    font-size: 14px;
    border-radius: 4px;
    box-sizing: border-box;
    cursor: pointer;
}
.next-btn2 {
    position: absolute;
    width: 80px;
    height: 40px;
    line-height: 40px;
    padding: 0 25px;
    margin-left: 390px;
    top: 500px;
    font-size: 14px;
    border-radius: 4px;
    box-sizing: border-box;
    cursor: pointer;
}
.next-btn3 {
    width: 80px;
    height: 40px;
    line-height: 40px;
    padding: 0 25px;
    margin-left: 70px;
    margin-top: -20px;
    font-size: 14px;
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
.upload-demo >>> .el-icon-upload {
    line-height: 0;
}
.upload-demo >>> .el-upload-dragger {
    width: 300px;
}
</style>