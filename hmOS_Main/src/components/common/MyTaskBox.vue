<template>
    <div class="Taskbox-wrapper">
        <div class="Taskbox-header">
            <span style="margin-left: 30px; font-size: 20px">任务类别:</span>
            <span style="margin-left: 20px; font-size: 20px; color: red">{{detail.type}}</span>
              <span style="margin-left: 30px; font-size: 20px">任务状态:</span>
            <span style="margin-left: 20px; font-size: 20px; color: red">{{detail.status}}</span>
        </div>
        <div class="Taskbox-body">
            <div class="task-detail-box">
                <div class="task-detail">
                    <span>任务名称:</span>
                    <span style="margin-left:10px;color:#499ec5" >{{detail.name}}</span>
                </div>
                <div class="task-detail">
                    <span>创建时间</span>
                    <span  style="margin-left:10px;color:#499ec5">{{detail.time}}</span>
                </div>
                <div class="task-detail">
                    <span>任务描述:</span>
                    <span  style="margin-left:10px;color:#499ec5">{{detail.description}}</span>
                </div>
                <div class="task-detail">
                    <span>任务要求:</span>
                    <span  style="margin-left:10px;color:#499ec5">{{detail.request}}</span>
                </div>
            </div>
            <div style="display:flex;justify-content:center;align-items: center;">
                   <i class="el-icon-edit"  style="font-size: 60px;color:green;cursor: pointer;" @click="goto()"></i>
                   <i class="el-icon-delete"  style="font-size: 60px;margin-left:40px;cursor: pointer;" ></i>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            tagsList: [],
            collapse: false
        };
    },
    props:["detail"],
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
                    path: `/humancomputingplus/${JSON.stringify(queryurl)}`
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
    }
};
</script>
<style>
.Taskbox-wrapper {
    width: 100%;
    height: 160px;
    margin: 10px;
    border-radius: 30px;
    border: 2px solid #c0c0c0;
    overflow: auto;
}
.Taskbox-header {
    height: 20%;
    background-color: #c0c0c0;
}
.Taskbox-body{
    height: 80%;
    background-color: #e4e2e2;
    display: flex;
    align-items: center;
    flex-wrap: wrap;
     /* background-color:#499ec5; */
}
.task-detail-box{
    margin-left:30px;
    float:left;
    display: flex;
    justify-content:center;
    align-items: center;
    flex-wrap: wrap;
    width:75%;
}
.task-detail{
    font-size:18px;
    width:50%;
    margin:10px 0 10px 0;
}
</style>
