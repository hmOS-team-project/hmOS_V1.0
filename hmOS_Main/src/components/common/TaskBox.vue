<template>
    <div class="Taskbox-wrapper">
        <div class="Taskbox-header">
            <span style="margin-left: 30px; font-size: 20px; color: rgb(0, 228, 255); font-weight: 400">Task Type:</span>
            <span style="margin-left: 20px; font-size: 20px; color: #ffffff; font-weight: 400">{{ detail.taskType }}</span>
            <span style="margin-left: 30px; font-size: 20px; color: rgb(0, 228, 255); font-weight: 400">Task State:</span>
            <span style="margin-left: 20px; font-size: 20px; color: #ffffff; font-weight: 400">{{ detail.taskStatus }}</span>
        </div>
        <div class="Taskbox-body">
            <div class="task-detail-box">
                <div class="task-detail">
                    <span>Task Name:</span>
                    <span style="margin-left: 10px; color: #ffffff">{{ detail.taskName }}</span>
                </div>
                <div class="task-detail">
                    <span>Create Time</span>
                    <span style="margin-left: 10px; color: #ffffff">{{ detail.startTime | formatDate }}</span>
                </div>
                <div class="task-detail">
                    <span>Task Description:</span>
                    <span style="margin-left: 10px; color: #ffffff">{{ detail.description }}</span>
                </div>
                <div class="task-detail">
                    <span>Task Requirement:</span>
                    <span style="margin-left: 10px; color: #ffffff">{{ detail.taskTimeRequire + ' ' + detail.taskAccRequire + '%' }}</span>
                </div>
            </div>
            <div style="display: flex; justify-content: center; align-items: center">
                <i class="el-icon-document" style="font-size: 60px; cursor: pointer" :style="{ color: detailColor }" @click="goto()"></i>
                <i class="el-icon-delete" style="font-size: 60px; color: #909399; margin-left: 40px; cursor: pointer"></i>
            </div>
        </div>
    </div>
</template>

<script>
import { formatdate } from '@/assets/js/date.js';
export default {
    data() {
        return {
            tagsList: [],
            collapse: false,
            detailColor: '',
            detailType: ''
        };
    },
    props: ['detail'],
    watch: {
        detail: function (newVal, oldVAl) {
            this.detailType = newVal.taskStatus;
            this.changeColor(this.detailType);
        }
    },
    methods: {
        goto() {
            let resulturl = {
                resulturl: this.detail.resultUrl,
                taskid: this.detail._id
            };
            let queryurl = {
                queryurl: this.detail.queryUrl
            };
            if (this.detail.taskStatus == 'Finished')
                this.$router.push({
                    path: `/computingresultplus/${JSON.stringify(resulturl)}`
                });
            else if (this.detail.taskStatus == 'Unexecuted')
                this.$router.push({
                    path: `/humancomputingpluss/${JSON.stringify(queryurl)}`
                });
            else
                this.$router.push({
                    path: `/humancomputingpluss/${JSON.stringify(queryurl)}`
                });
        },
        changeColor(type) {
            switch (type) {
                case 'Unexecuted':
                    this.detailColor = '#F56C6C';
                    break;
                case 'Executing':
                    this.detailColor = '#E6A23C';
                    break;
                case 'Finished':
                    this.detailColor = '#67C23A';
                    break;
            }
        }
    },
    filters: {
        formatDate(time) {
            var date = new Date(time);
            return formatdate(date, 'yyyy-MM-dd hh:mm:ss'); // 自定义的日期格式
        }
    }
};
</script>
<style>
.Taskbox-wrapper {
    width: 100%;
    height: 160px;
    margin: 10px;
    border-radius: 30px;
    /* border: 2px solid #58ACFA; */
    overflow: auto;
    box-shadow: 0px 0px 10px #837979;
    border-radius: 10px;
}
.Taskbox-header {
    height: 20%;
    background-color: rgba(3, 26, 37, 0.4);
}
.Taskbox-body {
    height: 80%;
    background-color: rgba(3, 26, 37, 0.4);
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    /* background-color:#499ec5; */
}
.task-detail-box {
    margin-left: 30px;
    float: left;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    width: 75%;
}
.task-detail {
    font-weight: 400;
    color: rgb(0, 228, 255);
    font-size: 18px;
    width: 50%;
    margin: 10px 0 10px 0;
}
</style>
