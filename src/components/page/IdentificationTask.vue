<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-lx-home"></i> 识别任务</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <el-row :gutter="18">
            <el-col :span="16"> 
                <el-card shadow="hover" style="height: 580px" :body-style="{ padding: '0px' }">
                    <div class="header-box1">
                        <img src="../../assets/img/icon-taskinput.png" style="width: 45px; height: 45px" />
                        <span style="color: white; font-size: 20px">任务输入</span>
                    </div>
                    <el-row :gutter="20">
                        <el-col :span="14">
                            <el-form ref="form" :model="form" label-width="90px">
                                <el-form-item label="任务名称">
                                    <el-col :span="20">
                                        <el-input></el-input>
                                    </el-col>
                                </el-form-item>
                                <el-form-item label="时间要求">
                                    <el-col :span="10">
                                        <el-input></el-input>
                                    </el-col>
                                </el-form-item>
                                <el-form-item label="精度要求">
                                    <el-col :span="10">
                                        <el-input></el-input>
                                    </el-col>
                                </el-form-item>
                                <el-form-item label="任务描述">
                                    <el-col :span="20">
                                        <el-input type="textarea" rows="8" v-model="form.desc"></el-input>
                                    </el-col>
                                </el-form-item>
                                <el-form-item label="资源配置">
                                    <el-col :span="20">
                                        <el-radio v-model="radio" :label="true">默认</el-radio>
                                        <el-radio v-model="radio" :label="false" @click="changestatus">自定义</el-radio>
                                    </el-col>
                                </el-form-item>
                            </el-form>
                        </el-col>
                        <el-col :span="7">
                            <span>待识别目标输入</span>
                            <div class="crop-demo">
                                <img :src="cropImg" class="pre-img" />
                                <div class="crop-btn-box">
                                    <div class="crop-demo-btn">
                                        选择图片
                                        <input class="crop-input" type="file" name="image" accept="image/*" @change="setImage" />
                                    </div>
                                    <div class="submit-crop-demo-btn">
                                        确认上传
                                        <input class="crop-input" type="submit" />
                                    </div>
                                </div>
                            </div>
                            <span>数据集输入</span>
                            <el-upload class="upload-demo" action="http://jsonplaceholder.typicode.com/api/posts/" multiple>
                                <i class="el-icon-upload"></i>
                                <div class="el-upload__text">将待检测视频或文本拖到此处，或<em>点击上传</em></div>
                                <!-- <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div> -->
                            </el-upload>
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
                    </el-row>
                    <div class="resourcenum">
                        <div class="resource-box">
                            <img src="../../assets/img/icon-user.png" style="display: block; width: 60px; height: 60px" />
                            <div class="number-box">
                                <div>普通用户</div>
                                <el-input-number
                                    v-model="num1"
                                    controls-position="right"
                                    :disabled="radio"
                                    :min="0"
                                    :max="100"
                                ></el-input-number>
                            </div>
                        </div>
                        <div class="resource-box">
                            <img src="../../assets/img/icon-exports.png" style="display: block; width: 60px; height: 60px" />
                            <div class="number-box">
                                <div>专业技术者</div>
                                <el-input-number
                                    v-model="num2"
                                    controls-position="right"
                                    :disabled="radio"
                                    :min="0"
                                    :max="100"
                                ></el-input-number>
                            </div>
                        </div>
                        <div class="resource-box">
                            <img src="../../assets/img/icon-gpu2.png" style="display: block; width: 60px; height: 60px" />
                            <div class="number-box">
                                <div>GPU</div>
                                <el-input-number
                                    v-model="num3"
                                    controls-position="right"
                                    :disabled="radio"
                                    :min="0"
                                    :max="100"
                                ></el-input-number>
                            </div>
                        </div>
                    </div>
                </el-card>
            </el-col>
            <el-col :span="8">
                <el-card shadow="hover" style="height: 580px" :body-style="{ padding: '0px' }">
                    <div class="header-box1">
                        <img src="../../assets/img/icon-typeselect.png" style="width: 45px; height: 45px" />
                        <span style="color: white; font-size: 20px">模型搭建</span>
                    </div>
                    <div class="button-box">
                        <el-radio v-model="radio5" :label="true" border>  默认</el-radio>
                        <el-radio v-model="radio5" :label="false" border>自定义</el-radio>
                    </div>
                    <div class="net-box">
                        <div class="net-name">网络结构</div>
                        <div class="net-select">
                            <el-radio-group v-model="radio2" :disabled="radio5">
                                <td>
                                    <el-radio :label="1">Faster R-CNN</el-radio>
                                </td>
                                <td>
                                    <el-radio :label="2">Mask R-CNN</el-radio>
                                </td>
                                <tr></tr>
                                <td>
                                    <el-radio :label="3">Cascade R-CNN</el-radio>
                                </td>
                                <td>
                                    <el-radio :label="4">SSD</el-radio>
                                </td>
                                <tr></tr>
                                <td>
                                    <el-radio :label="5">YOLOv3</el-radio>
                                </td>
                                <td>
                                    <el-radio :label="6">RetinaNet</el-radio>
                                </td>
                                <tr></tr>
                                <td>
                                    <el-radio :label="7">SSDLite</el-radio>
                                </td>
                            </el-radio-group>
                        </div>
                    </div>
                    <div class="net-box">
                        <div class="net-name">骨干网络</div>
                        <div class="net-select">
                            <el-radio-group v-model="radio3" :disabled="radio5">
                                <td>
                                    <el-radio :label="1">ResNet-vd</el-radio>
                                </td>
                                <td>
                                    <el-radio :label="2">ResNet</el-radio>
                                </td>
                                <tr></tr>
                                <td>
                                    <el-radio :label="3">Mobilenet V1/V3</el-radio>
                                </td>
                                <td>
                                    <el-radio :label="4">SENet</el-radio>
                                </td>
                                <tr></tr>
                                <td>
                                    <el-radio :label="6">Res2Net</el-radio>
                                </td>
                                <td>
                                    <el-radio :label="7">HRNet</el-radio>
                                </td>
                            </el-radio-group>
                        </div>
                    </div>
                    <div class="net-box">
                        <div class="net-name">扩展模块</div>
                        <div class="net-select">
                            <el-radio-group v-model="radio4" :disabled="radio5">
                                <td>
                                    <el-radio :label="1">Non-Local Network</el-radio>
                                </td>
                                <td>
                                    <el-radio :label="2">FPN</el-radio>
                                </td>
                                <tr></tr>
                                <td>
                                    <el-radio :label="3">Group Norm</el-radio>
                                </td>
                                <td>
                                    <el-radio :label="4">IoU/DIoU Loss</el-radio>
                                </td>
                                <tr></tr>
                                <td>
                                    <el-radio :label="5">IoU Aware</el-radio>
                                </td>
                            </el-radio-group>
                        </div>
                    </div>
                    <div class="next-btn" @click="taskmode()">
                        下一步
                        <input class="crop-input" type="submit" />
                    </div>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import Schart from 'vue-schart';
import bus from '../common/bus';
import VueCropper from 'vue-cropperjs';
export default {
    name: 'dashboard',
    data: function () {
        return {
            radio: true,
            radio1: '1',
            radio2: '0',
            radio3: '0',
            radio4: '0',
            radio5: true,
            num1: 0,
            num2: 0,
            num3: 0,
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
        VueCropper
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
        taskmode(){
             this.$router.push('/taskmode');
        },
        changeDate() {
            const now = new Date().getTime();
            this.data.forEach((item, index) => {
                const date = new Date(now - (6 - index) * 86400000);
                item.name = `${date.getFullYear()}/${date.getMonth() + 1}/${date.getDate()}`;
            });
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
        imageuploaded(res) {
            console.log(res);
        },
        handleError() {
            this.$notify.error({
                title: '上传失败',
                message: '图片上传接口上传失败，可更改为自己的服务器接口'
            });
        }
        // handleListener() {
        //     bus.$on('collapse', this.handleBus);
        //     // 调用renderChart方法对图表进行重新渲染
        //     window.addEventListener('resize', this.renderChart);
        // },
        // handleBus(msg) {
        //     setTimeout(() => {
        //         this.renderChart();
        //     }, 200);
        // },
        // renderChart() {
        //     this.$refs.bar.renderChart();
        //     this.$refs.line.renderChart();
        // }
    },
    created() {
        this.cropImg = this.defaultSrc;
    }
};
</script>


<style scoped>
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
    margin-left: 150px;
    margin-top: 10px;
    background-color: #409eff;
    color: #fff;
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
    width: 200px;
    height: 50px;
    background: url('../../assets/img/icon-typebackground.png') no-repeat;
    background-size: 100% 100%;
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}
.resource-box {
    display: flex;
    text-align: center;
    margin-left: 50px;
}
.resourcenum {
    display: flex;
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
    justify-content: center;
    padding: 5px;
    background: #EDEDED;
    margin: 20px 5px 20px 5px;
}
.net-name {
    display: flex;
    width: 100px;
    height: 50px;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    font-weight: 800;
}
.net-select {
    width: 250px;
    height: 100px;
    display: flex;
    align-items: center;
}
</style>
