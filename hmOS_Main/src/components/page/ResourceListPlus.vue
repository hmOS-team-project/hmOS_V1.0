<template>
    <div>
        <div id='loading' style='display: none'>
            <div class='loadEffect'>
                <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
            </div>
        </div>
        <!--标题栏-->
        <div class='Hometitlebox'>
            <img src='../../assets/img/logo2.png' style='width: 50px; height: 50px; margin-right: 25px' />
            <a style='color: #00e4ff'>hmOS1.0</a>
            <img src='../../assets/img/logo1.png' style='width: 60px; height: 50px; margin-left: 15px' />
        </div>
        <el-row :gutter='20' style='margin-top:45px'>
            <el-col :span='12'>
                <div class='resourcelist_card'>
                    <el-card style='margin-left: 30px'>
                        <el-row :gutter='20'>
                            <el-col :span='3'>
                                <div style='margin-top: -6px'>
                                    <img src='../../assets/img/personIcon.png' class='personIcon'
                                         style='width: 50px; height: 50px;' />
                                </div>
                            </el-col>
                            <el-col :span='12'>
                                <el-input placeholder='Please enter the contents'>
                                    <el-button slot='append' icon='el-icon-search'></el-button>
                                </el-input>
                            </el-col>
                            <el-col :span='4' style='margin-left: 145px'>
                                <el-button type='primary' class='addButton' @click='addHumanDialog = true'>Add
                                </el-button>
                            </el-col>
                        </el-row>
                        <el-table :data='humanlist' border stripe style='margin-top: 15px'>
                            <el-table-column label='No' type='index'></el-table-column>
                            <el-table-column label='Name' prop='username' align='center'></el-table-column>
                            <el-table-column label='Phone' prop='mobile' align='center'></el-table-column>
                            <el-table-column label='Major' prop='profession' align='center'></el-table-column>
                            <el-table-column label='Speciality' prop='strength' align='center'></el-table-column>
                            <el-table-column label='Status' align='center' width='80%'>
                                <template slot-scope='scope'>
                                    <el-switch v-model='scope.row.mg_state'
                                               @change='userStateChanged(scope.row)'></el-switch>
                                </template>
                            </el-table-column>
                            <el-table-column label='Details' align='center' width='80%'>
                                <template slot-scope='scope'>
                                    <!-- 查看按钮 -->
                                    <el-button type='primary' icon='el-icon-plus' size='mini'
                                               @click='checkHumanDetail'></el-button>
                                </template>
                            </el-table-column>
                            <el-table-column label='Operation' align='center'>
                                <template slot-scope='scope'>
                                    <el-button type='primary' icon='el-icon-edit' size='mini' circle></el-button>
                                    <el-button type='danger' icon='el-icon-delete' size='mini' circle></el-button>
                                </template>
                            </el-table-column>
                        </el-table>
                        <el-pagination small layout='prev, pager, next' :total='50'
                                       style='margin-top: 10px'></el-pagination>
                        <el-dialog title='Add Human Resource' :visible.sync='addHumanDialog' width='35%'
                                   :before-close='handleClose'>
                            <el-form ref='form' :model='form' label-width='80px'>
                                <el-form-item label='Name'>
                                    <el-input v-model='form.name'></el-input>
                                </el-form-item>
                                <el-form-item label='Phone'>
                                    <el-input v-model='form.mobile'></el-input>
                                </el-form-item>
                                <el-form-item label='Major'>
                                    <el-input v-model='form.profession'></el-input>
                                </el-form-item>
                                <el-form-item label='Speciality'>
                                    <el-checkbox-group v-model='form.type1'>
                                        <el-checkbox label='identify' name='type'></el-checkbox>
                                        <el-checkbox label='generate' name='type'></el-checkbox>
                                        <el-checkbox label='sensing' name='type'></el-checkbox>
                                        <el-checkbox label='others' name='type'></el-checkbox>
                                    </el-checkbox-group>
                                </el-form-item>
                                <el-form-item label='不喜欢'>
                                    <el-checkbox-group v-model='form.type2'>
                                        <el-checkbox label='identify' name='type'></el-checkbox>
                                        <el-checkbox label='generate' name='type'></el-checkbox>
                                        <el-checkbox label='sensing' name='type'></el-checkbox>
                                        <el-checkbox label='others' name='type'></el-checkbox>
                                    </el-checkbox-group>
                                </el-form-item>
                            </el-form>
                            <!-- 底部按钮区 -->
                            <span slot='footer' class='dialog-footer'>
                                <el-button @click='addHumanDialog = false'>取 消</el-button>
                                <el-button type='primary' @click='addHumanDialog = false'>确 定</el-button>
                            </span>
                        </el-dialog>
                    </el-card>
                </div>
            </el-col>
            <el-col :span='12'>
                <div class='resourcelist_card'>
                    <el-card style='margin-right: 30px'>
                        <el-row :gutter='20'>
                            <el-col :span='3'>
                                <div style='margin-top: -6px'>
                                    <img src='../../assets/img/machine.png' class='personIcon'
                                         style='width: 50px; height: 50px;' />
                                </div>
                            </el-col>
                            <el-col :span='12'>
                                <el-input placeholder='Please enter the contents'>
                                    <el-button slot='append' icon='el-icon-search'></el-button>
                                </el-input>
                            </el-col>
                            <el-col :span='4' style='margin-left: 145px'>
                                <el-button type='primary' class='addButton' @click='addMachineDialog = true'>Add
                                </el-button>
                            </el-col>
                        </el-row>
                        <el-table border stripe style='margin-top: 15px' :data="machinelist">
                            <el-table-column label='No' type='index'></el-table-column>
                            <el-table-column label='IP' prop='ip' align='center'></el-table-column>
                            <el-table-column label='CPU' prop='cpu' align='center'></el-table-column>
                            <el-table-column label='GPU' prop='gpu' align='center'></el-table-column>
                            <el-table-column label='Memory' prop='resource' align='center'></el-table-column>
                            <el-table-column label='Status' width='80%' align='center'>
                                <template slot-scope='scope'>
                                    <el-switch v-model='scope.row.mg_state'
                                               @change='userStateChanged(scope.row)'></el-switch>
                                </template>
                            </el-table-column>
                            <el-table-column label='Details' width='80%' align='center'>
                                <template slot-scope='scope'>
                                    <!-- 查看按钮 -->
                                    <el-button type='primary' icon='el-icon-plus' size='mini'
                                               @click='checkHumanDetail'></el-button>
                                </template>
                            </el-table-column>
                            <el-table-column label='Operation' align='center'>
                                <template slot-scope='scope'>
                                    <el-button type='primary' icon='el-icon-edit' size='mini' circle></el-button>
                                    <el-button type='danger' icon='el-icon-delete' size='mini' circle></el-button>
                                </template>
                            </el-table-column>
                        </el-table>
                        <el-pagination small layout='prev, pager, next' :total='50'
                                       style='margin-top: 10px'></el-pagination>
                        <el-dialog title='Add Machine resource' :visible.sync='addMachineDialog' width='35%'
                                   :before-close='handleClose'>
                            <el-form ref='mform' :model='mform' label-width='80px'>
                                <el-form-item label='IP'>
                                    <el-input v-model='mform.ip'></el-input>
                                </el-form-item>
                                <el-form-item label='CPU'>
                                    <el-input v-model='mform.cpu'></el-input>
                                </el-form-item>
                                <el-form-item label='GPU'>
                                    <el-input v-model='mform.gpu'></el-input>
                                </el-form-item>
                                <el-form-item label='内存'>
                                    <el-radio-group v-model='mform.resource'>
                                        <el-radio label='4G'></el-radio>
                                        <el-radio label='8G'></el-radio>
                                        <el-radio label='16G'></el-radio>
                                    </el-radio-group>
                                </el-form-item>
                                <el-form-item label='显存'>
                                    <el-radio-group v-model='mform.resource'>
                                        <el-radio label='1G'></el-radio>
                                        <el-radio label='2G'></el-radio>
                                        <el-radio label='4G'></el-radio>
                                    </el-radio-group>
                                </el-form-item>
                                <el-form-item label='外存'>
                                    <el-radio-group v-model='mform.resource'>
                                        <el-radio label='128G'></el-radio>
                                        <el-radio label='256G'></el-radio>
                                        <el-radio label='512G'></el-radio>
                                        <el-radio label='1T'></el-radio>
                                        <el-radio label='2T'></el-radio>
                                        <el-radio label='4T'></el-radio>
                                    </el-radio-group>
                                </el-form-item>
                            </el-form>
                            <!-- 底部按钮区 -->
                            <span slot='footer' class='dialog-footer'>
                            <el-button @click='addMachineDialog = false'>取 消</el-button>
                            <el-button type='primary' @click='addMachineDialog = false'>确 定</el-button>
                            </span>
                        </el-dialog>
                    </el-card>
                </div>
            </el-col>
        </el-row>
        <div class='copyrigntoutbox'>
            <span class='copyrigntmsg'>Copyright © 2020 Northwestern Polytechnical University All Rights Reserved</span>
        </div>
    </div>
</template>

<script>
import Schart from 'vue-schart';
import bus from '../common/bus';
import VueCropper from 'vue-cropperjs';
import '@/assets/css/style.css';
import '@/assets/css/normalize.min.css';
import '@/assets/js/index.js.下载';
import '@/assets/css/Datacages_Homeindex.css';

export default {
    name: 'ResourceListPlus',
    data() {
        return {
            humanlist: [{
                username: 'Alice',
                mobile: '15379316701',
                profession: '翻译',
                strength: '生成类',
                dislike: '',
                ability_score: '90'
            }, {
                username: 'Bob',
                mobile: '15379316701',
                profession: '翻译',
                strength: '生成类',
                dislike: '',
                ability_score: '90'
            }, {
                username: 'John',
                mobile: '15379316701',
                profession: '翻译',
                strength: '生成类',
                dislike: '',
                ability_score: '90'
            }, {
                username: 'Alex',
                mobile: '15379316701',
                profession: '翻译',
                strength: '生成类',
                dislike: '',
                ability_score: '90'
            }, {
                username: 'Jenny',
                mobile: '15379316701',
                profession: '翻译',
                strength: '生成类',
                dislike: '',
                ability_score: '90'
            }, {
                username: 'Alice',
                mobile: '15379316701',
                profession: '翻译',
                strength: '生成类',
                dislike: '',
                ability_score: '90'
            }],
            machinelist: [{
                ip: '192.168.0.1:8000',
                cpu: 'Intel Core i5-8500',
                gpu: 'NVIDIA GTX1080Ti',
                resource: '16GB',
            }, {
                ip: '192.168.0.1:8000',
                cpu: 'Intel Core i5-8500',
                gpu: 'NVIDIA GTX1080Ti',
                resource: '16GB',
            },{
                ip: '192.168.0.1:8000',
                cpu: 'Intel Core i5-8500',
                gpu: 'NVIDIA GTX1080Ti',
                resource: '16GB',
            },{
                ip: '192.168.0.1:8000',
                cpu: 'Intel Core i5-8500',
                gpu: 'NVIDIA GTX1080Ti',
                resource: '16GB',
            },{
                ip: '192.168.0.1:8000',
                cpu: 'Intel Core i5-8500',
                gpu: 'NVIDIA GTX1080Ti',
                resource: '16GB',
            },{
                ip: '192.168.0.1:8000',
                cpu: 'Intel Core i5-8500',
                gpu: 'NVIDIA GTX1080Ti',
                resource: '16GB',
            }],
            addHumanDialog: false,
            form: {
                name: '',
                mobile: '',
                profession: '',
                type1: [],
                type2: []
            },
            addMachineDialog: false,
            mform: {
                ip: '',
                cpu: '',
                gpu: '',
                resource: ''
            }
        };
    },
    methods: {
        checkHumanDetail() {
            this.$router.push('/humanDetail');
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
h3,
ul,
li {
    margin: 0;
    padding: 0;
    list-style: none;
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

.resourcelist_card >>> .el-card {
    background-color: rgba(5, 53, 77, 0.7);
    border: 1px solid #ebeef500;
    color: rgb(0, 228, 255);
    font-weight: bold;
}

.resourcelist_card >>> .el-input__inner {
    background-color: rgba(5, 53, 77, 0.7);
    border: 1px solid #00e4ff;
    color: #00e4ff;
}

.resourcelist_card >>> .el-input-group__append {
    color: #00e4ff;
    background-color: rgba(5, 53, 77, 0.7);
    border: 1px solid #00e4ff;
}

.resourcelist_card >>> .el-input-group__prepend {
    color: #00e4ff;
    background-color: rgbargba(5, 53, 77, 0.7);
    border: 1px solid #00e4ff;
}

.resourcelist_card >>> .el-table {
    background-color: rgba(0, 168, 255, 0.2);
    color: #00e4ff;
}

.resourcelist_card >>> .el-table--striped .el-table__body tr.el-table__row--striped td {
    background: rgba(0, 168, 255, 0.2);
}

.resourcelist_card >>> .el-table--border td, .el-table--border th, .el-table__body-wrapper .el-table--border.is-scrolling-left ~ .el-table__fixed {
    border-bottom: 1px solid #00e4ff;
}

.resourcelist_card >>> .el-table--border td, .el-table--border th, .el-table__body-wrapper .el-table--border.is-scrolling-left ~ .el-table__fixed {
    border-right: 1px solid #00e4ff;
}

.resourcelist_card >>> .el-button {
    color: #00e4ff;
    background-color: rgba(0, 168, 255, 0.2);
    border: 1px solid #00e4ff;
}

.resourcelist_card >>> .el-pagination button:disabled {
    color: #00e4ff;
    background-color: rgba(0, 168, 255, 0.6);
}

.resourcelist_card >>> .el-pagination button:enabled {
    color: #00e4ff;
    background-color: rgba(0, 168, 255, 0.6);
}

.resourcelist_card >>> .el-pager li.active {
    color: #00e4ff;
}

.resourcelist_card >>> .el-pager li {
    background-color: rgba(0, 168, 255, 0.2);
}

.resourcelist_card >>> .el-table th.is-leaf {
    border-bottom: 2px solid #00e4ff;
    border-right: 2px solid #00e4ff;
}

.resourcelist_card >>> .el-table th {
    background-color: rgba(0, 168, 255, 0.2) !important;
}

.resourcelist_card >>> .el-table tr {
    background-color: rgba(0, 168, 255, 0.2) !important;
}

.resourcelist_card >>> .el-table thead {
    color: #00e4ff;
}

.resourcelist_card >>> .el-table--border {
    border: 1px solid #00e4ff;
}

.resourcelist_card >>> .el-pagination {
    color: #849dce;
}

.resourcelist_card >>> .el-table tbody tr:hover > td {
    background-color: rgba(8, 95, 130, 0.8) !important
}
.resourcelist_card >>> .el-dialog, .el-pager li
{
    background: rgb(7, 81, 109);
}
.resourcelist_card >>> .el-dialog__title
{
    color:#00e4ff;
}
.resourcelist_card >>> .el-form-item__label
{
    color:#00e4ff;
}
.resourcelist_card >>> .el-checkbox
{
    color:#00e4ff;
}
.resourcelist_card >>> .el-radio
{
    color:#00e4ff;
}

</style>