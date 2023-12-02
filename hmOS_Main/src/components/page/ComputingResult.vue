<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb>
                <el-breadcrumb-item><i class="el-icon-finished"></i> 计算结果查看</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <!-- <div class="container">
            <div class="plugins-tips">
                mavonEditor：基于Vue的markdown编辑器。
                访问地址：<a href="https://github.com/hinesboy/mavonEditor" target="_blank">mavonEditor</a>
            </div>
            <mavon-editor v-model="content" ref="md" @imgAdd="$imgAdd" @change="change" style="min-height: 600px"/>
            <el-button class="editor-btn" type="primary" @click="submit">提交</el-button>
        </div> -->
        <el-row :gutter="20">
            <el-col :span="12">
                <el-card shadow="hover" style="height: 580px" >
                    <div slot="header" class="clearfix">
                        <span>计算结果输出</span>
                    </div>
                    <!-- <video src="../../assets/img/tokyo-street.mp4" controls="controls" class="video"></video> -->
                    <el-button type="primary" style=" height: 30px; width: 75px">下载结果</el-button>
                    <el-table :data="tableData" style="width: 100%">
                        <el-table-column prop="date" label="帧数" width="180"> </el-table-column>
                        <el-table-column prop="name" label="左上角坐标" width="180"> </el-table-column>
                        <el-table-column prop="address" label="右下角坐标"> </el-table-column>
                        <el-table-column prop="conf" label="置信度"> </el-table-column>
                    </el-table>
                </el-card>
            </el-col>
            <el-col :span="12">
                <el-card shadow="hover" style="height: 580px">
                    <div slot="header" class="clearfix">
                        <span>计算过程详情</span>
                    </div>
               <el-tag type="info" size="big" style="width:132px;height:40px;font-size:18px; margin-left:20px">参与计算人数:</el-tag>
                <el-tag type="success" size="big" style="width:60px;height:40px;font-size:18px;margin-left:20px">五人</el-tag>
                  <el-tag type="info" size="big" style="width:132px;height:40px;font-size:18px; margin-left:20px">参与计算GPU:</el-tag>
                    <el-tag type="success" size="big" style="width:125px;height:40px;font-size:18px; margin-left:20px">5*RTX TITAN</el-tag>
                    <div style="margin-bottom:30px"></div>
                   <el-tag type="info" size="big" style="width:132px;height:40px;font-size:18px; margin-left:20px;text-align: center">分配策略:</el-tag>
                    <el-tag type="success" size="big" style="width:115px;height:40px;font-size:18px; margin-left:10px">分配策略一</el-tag>
                <el-tag type="info" size="big" style="width:132px;height:40px;font-size:18px; margin-left:20px;text-align: center">融合策略:</el-tag>
                <el-tag type="success" size="big" style="width:127px;height:40px;font-size:18px;margin-left:10px;text-align: center">融合策略一</el-tag>
                 <div style="margin-bottom:30px"></div>
                   <el-tag type="info" size="big" style="width:132px;height:40px;font-size:18px; margin-left:20px;text-align: center">计算模式:</el-tag>
                    <el-tag type="success" size="big" style="width:123px;height:40px;font-size:18px; margin-left:10px">人机并行计算</el-tag>
                <el-tag type="info" size="big" style="width:132px;height:40px;font-size:18px; margin-left:20px;text-align: center">占用存储:</el-tag>
                <el-tag type="success" size="big" style="width:70px;height:40px;font-size:18px;margin-left:10px;text-align: center">20G</el-tag>
                <div style="margin-bottom:30px"></div>
                  <el-tag type="info" size="big" style="width:132px;height:40px;font-size:18px; margin-left:0px;text-align: center">任务开始时间:</el-tag>
                    <el-tag type="success" size="big" style="width:144px;height:40px;font-size:18px; margin-left:5px">2020/11/1 10:00</el-tag>
                <el-tag type="info" size="big" style="width:132px;height:40px;font-size:18px; margin-left:10px;text-align: center">任务结束时间:</el-tag>
                <el-tag type="success" size="big" style="width:144px;height:40px;font-size:18px;margin-left:5px;text-align: center">2020/11/1 20:30</el-tag>
              <div style="margin-bottom:30px"></div>
                   <el-tag type="info" size="big" style="width:132px;height:40px;font-size:18px; margin-left:20px;text-align: center">识别精度:</el-tag>
                    <el-tag type="success" size="big" style="width:60px;height:40px;font-size:18px; margin-left:20px">95%</el-tag>
                <el-tag type="info" size="big" style="width:132px;height:40px;font-size:18px; margin-left:20px">计算消耗时间:</el-tag>
                <el-tag type="success" size="big" style="width:127px;height:40px;font-size:18px;margin-left:20px">10小时30分钟</el-tag>
              <div style="margin-bottom:30px"></div>
                    <el-tag type="info" size="big" style="width:132px;height:40px;font-size:18px; margin-left:20px;text-align: center">迭代轮数:</el-tag>
                    <el-tag type="success" size="big" style="width:115px;height:40px;font-size:18px; margin-left:20px;text-align: center">五轮</el-tag>
              <div style="margin-bottom:30px"></div>
                    <el-button type="primary" style="margin-left: 200px; height: 50px; width: 100px">接受结果</el-button>
                      <el-button type="primary" style="margin-left: 30px; height: 50px; width: 100px">重新迭代</el-button>
                </el-card>
            </el-col>
        </el-row>

        <!-- <div class="container1">
            <div class="container1-box1">
                <div class="container1-box11">
                    <video src="../../assets/img/tokyo-street.mp4" controls="controls" class="video"></video>
                </div>
            </div>
            <div class="container1-box2">
               	<div class="result">结 果</div>
                <div class="table">
                    <table border="1">
                        <tr>
                            <td>坐标/帧数</td>
                            <th>第一个坐标</th>
                            <th>第二个坐标</th>
                        </tr>
                        <tr>
                            <td align="center">1</td>
                            <td align="center">(60,30)</td>
                            <td align="center">(90,80)</td>
                        </tr>
                        <tr>
                            <td align="center">2</td>
                            <td align="center">(50,30)</td>
                            <td align="center">(80,80)</td>
                        </tr>
                        <tr>
                            <td align="center">3</td>
                            <td align="center">(20,30)</td>
                            <td align="center">(50,80)</td>
                        </tr>
                    </table>
                </div>
            </div>
        </div> -->
    </div>
</template>

<script>
import { mavonEditor } from 'mavon-editor';
import 'mavon-editor/dist/css/index.css';
export default {
    name: 'markdown',
    data: function () {
        return {
            content: '',
            html: '',
            configs: {},
            tableData: [{
            date: 'c4s3_008073',
            name: '(2,2)',
            address: '(20,20)',
            conf: '0.95'
          }, {
            date: 'c4s3_008094',
            name: '(3,3)',
            address: '(30,30)',
            conf: '0.94'
          }, {
            date: 'c4s3_008123',
            name: '(4,4)',
            address: '(50,50)',
            conf: '0.96'
          }, {
            date: 'c4s3_008158',
            name: '(6,6)',
            address: '(80,80)',
            conf: '0.98'
          }]
        };
    },
    components: {
        mavonEditor
    },
    methods: {
        // 将图片上传到服务器，返回地址替换到md中
        $imgAdd(pos, $file) {
            var formdata = new FormData();
            formdata.append('file', $file);
            // 这里没有服务器供大家尝试，可将下面上传接口替换为你自己的服务器接口
            this.$axios({
                url: '/common/upload',
                method: 'post',
                data: formdata,
                headers: { 'Content-Type': 'multipart/form-data' }
            }).then((url) => {
                this.$refs.md.$img2Url(pos, url);
            });
        },
        change(value, render) {
            // render 为 markdown 解析后的结果
            this.html = render;
        },
        submit() {
            console.log(this.content);
            console.log(this.html);
            this.$message.success('提交成功！');
        }
    }
};
</script>
<style scoped>
/*   .editor-btn{
        margin-top: 20px;
    } */

.container1-box1 {
    position: absolute;
    width: 600px;
    height: 450px;
    /* background-color: black; */
    border: 1px solid #000;
}
.container1-box11 {
    position: relative;
    width: 500px;
    height: 300px;
    margin-left: 50px;
    margin-top: 40px;
    /* background-color: white; */
}
.video {
    width: 495px;
    height: 300px;
}

.container1-box2 {
    position: absolute;
    width: 500px;
    height: 450px;
    margin-left: 650px;
    border: 1px solid #000;
}
.result {
    text-align: center;
    font-size: 30px;
    margin-top: 40px;
}
.table {
    width: 500px;
    height: 450px;
    margin-top: 40px;
    margin-left: 100px;
}
</style>