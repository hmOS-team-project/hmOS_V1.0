<template>
    <div>
     <el-row :gutter="20">
            <el-col :span="12">
      <!-- 卡片视图区 -->
      <el-card>
          <!-- 搜索与添加区域 -->
          <el-row :gutter="20">
            <el-col :span="6">
              <div><img src="../../assets/img/personIcon.png" class="personIcon"/></div>
            </el-col>
            <!-- 搜索按钮 -->
            <el-col :span="6">
              <!-- <el-input placeholder="请输入内容" clearable @clear="getUserList">
                <el-button slot="append" icon="el-icon-search" @click="getUserList"></el-button>
              </el-input> -->
            </el-col>
            <!-- 添加按钮 -->
            <el-col :span="6">
              <el-button type="primary" class="addButton" @click="addHumanDialog = true">添加</el-button>
            </el-col>
          </el-row>
          <!-- 人类列表区 -->
          <el-table :data="humanlist" border stripe style="width: 100%">
            <el-table-column type="index" label="No"></el-table-column>
            <el-table-column label="姓名" prop="username"></el-table-column>
            <el-table-column label="电话" prop="mobile"></el-table-column>
            <el-table-column label="专业" prop="profession"></el-table-column>
            <el-table-column label="擅长" prop="strength"></el-table-column>
            <el-table-column label="状态">
              <!-- 定义一个作用域插槽渲染状态栏一列，通过slot-scope接受数据 -->
              <template slot-scope="scope">
                <el-switch v-model="scope.row.mg_state" @change="userStateChanged(scope.row)"></el-switch>
              </template>
            </el-table-column>
            <el-table-column label="查看详情">
              <template slot-scope="scope">
                <!-- 查看按钮 -->
                <el-button type="primary" icon="el-icon-plus" size="mini" @click="checkHumanDetail"></el-button>
              </template>
            </el-table-column>
          </el-table>
          <!-- 分页区域 -->
          <el-pagination small layout="prev, pager, next" :total="50"></el-pagination>
          <!-- 添加人类对话框 -->
          <el-dialog title="添加人类" :visible.sync="addHumanDialog" width="35%" :before-close="handleClose">
            <el-form ref="form" :model="form" label-width="80px">
              <el-form-item label="姓名">
                <el-input v-model="form.name"></el-input>
              </el-form-item>
              <el-form-item label="电话">
                <el-input v-model="form.mobile"></el-input>
              </el-form-item>
              <el-form-item label="专业">
                <el-input v-model="form.profession"></el-input>
              </el-form-item>
              <el-form-item label="擅长">
                <el-checkbox-group v-model="form.type">
                  <el-checkbox label="识别" name="type"></el-checkbox>
                  <el-checkbox label="生成" name="type"></el-checkbox>
                  <el-checkbox label="感知" name="type"></el-checkbox>
                  <el-checkbox label="其他" name="type"></el-checkbox>
                </el-checkbox-group>
              </el-form-item>
              <el-form-item label="不喜欢">
                <el-checkbox-group v-model="form.type">
                  <el-checkbox label="识别" name="type"></el-checkbox>
                  <el-checkbox label="生成" name="type"></el-checkbox>
                  <el-checkbox label="感知" name="type"></el-checkbox>
                  <el-checkbox label="其他" name="type"></el-checkbox>
                </el-checkbox-group>
              </el-form-item>
            </el-form>
            <!-- 底部按钮区 -->
            <span slot="footer" class="dialog-footer">
              <el-button @click="addHumanDialog = false">取 消</el-button>
              <el-button type="primary" @click="addHumanDialog = false">确 定</el-button>
            </span>
          </el-dialog>
      </el-card>
        </el-col>
          <el-col :span="12">
      <!-- 卡片视图区 -->
      <el-card >
          <!-- 搜索与添加区域 -->
          <el-row :gutter="20">
            <el-col :span="6">
              <div><img src="../../assets/img/machine.png" class="personIcon"/></div>
            </el-col>
            <el-col :span="6">
              <!-- <el-input placeholder="请输入内容" clearable @clear="getUserList">
                <el-button slot="append" icon="el-icon-search" @click="getUserList"></el-button>
              </el-input> -->
            </el-col>
            <el-col :span="6">
              <el-button type="primary" class="addButton" @click="addMachineDialog = true">添加</el-button>
            </el-col>
          </el-row>
          <!-- 机器列表区 -->
          <el-table :data="machinelist" border stripe style="width: 100%">
            <el-table-column type="index" label="No"></el-table-column>
            <el-table-column label="位置" prop="ip"></el-table-column>
            <el-table-column label="CPU" prop="cpu"></el-table-column>
            <el-table-column label="GPU" prop="gpu"></el-table-column>
            <el-table-column label="内存" prop="memory"></el-table-column>
            <el-table-column label="显存" prop="vram"></el-table-column>
            <el-table-column label="外存" prop="disk"></el-table-column>
            <el-table-column label="状态">
              <!-- 定义一个作用域插槽渲染状态栏一列，通过slot-scope接受数据 -->
              <template slot-scope="scope">
                <el-switch v-model="scope.row.mg_state" @change="userStateChanged(scope.row)"></el-switch>
              </template>
            </el-table-column>
            <el-table-column label="查看详情">
              <template slot-scope="scope">
                <!-- 查看按钮 -->
                <el-button type="primary" icon="el-icon-plus" size="mini"></el-button>
              </template>
            </el-table-column>
          </el-table>
          <!-- 分页区域 -->
          <el-pagination small layout="prev, pager, next" :total="50"></el-pagination>
          <!-- 添加人类对话框 -->
          <el-dialog title="添加机器" :visible.sync="addMachineDialog" width="35%" :before-close="handleClose">
            <el-form ref="mform" :model="mform" label-width="80px">
              <el-form-item label="定位">
                <el-input v-model="mform.ip"></el-input>
              </el-form-item>
              <el-form-item label="CPU">
                <el-input v-model="mform.cpu"></el-input>
              </el-form-item>
              <el-form-item label="GPU">
                <el-input v-model="mform.gpu"></el-input>
              </el-form-item>
              <el-form-item label="内存">
                <el-radio-group v-model="mform.resource">
                  <el-radio label="4G"></el-radio>
                  <el-radio label="8G"></el-radio>
                  <el-radio label="16G"></el-radio>
                </el-radio-group>
              </el-form-item>
              <el-form-item label="显存">
                <el-radio-group v-model="mform.resource">
                  <el-radio label="1G"></el-radio>
                  <el-radio label="2G"></el-radio>
                  <el-radio label="4G"></el-radio>
                </el-radio-group>
              </el-form-item>
              <el-form-item label="外存">
                <el-radio-group v-model="mform.resource">
                  <el-radio label="128G"></el-radio>
                  <el-radio label="256G"></el-radio>
                  <el-radio label="512G"></el-radio>
                  <el-radio label="1T"></el-radio>
                  <el-radio label="2T"></el-radio>
                  <el-radio label="4T"></el-radio>
                </el-radio-group>
              </el-form-item>
            </el-form>
            <!-- 底部按钮区 -->
            <span slot="footer" class="dialog-footer">
              <el-button @click="addMachineDialog = false">取 消</el-button>
              <el-button type="primary" @click="addMachineDialog = false">确 定</el-button>
            </span>
          </el-dialog>
      </el-card>
        </el-col>
          </el-row>

    </div>
</template>

<script>
export default {
  data () {
      return {
          humanlist: [{
              username: 'Alice',
              mobile: '15379316701',
              profession: '翻译',
              strength: '生成类',
              dislike: '',
              ability_score: '90'
          },{
              username: 'Alice',
              mobile: '15379316701',
              profession: '翻译',
              strength: '生成类',
              dislike: '',
              ability_score: '90'
          },{
              username: 'Alice',
              mobile: '15379316701',
              profession: '翻译',
              strength: '生成类',
              dislike: '',
              ability_score: '90'
          },{
              username: 'Alice',
              mobile: '15379316701',
              profession: '翻译',
              strength: '生成类',
              dislike: '',
              ability_score: '90'
          },{
              username: 'Alice',
              mobile: '15379316701',
              profession: '翻译',
              strength: '生成类',
              dislike: '',
              ability_score: '90'
          },{
              username: 'Alice',
              mobile: '15379316701',
              profession: '翻译',
              strength: '生成类',
              dislike: '',
              ability_score: '90'
          },{
              username: 'Alice',
              mobile: '15379316701',
              profession: '翻译',
              strength: '生成类',
              dislike: '',
              ability_score: '90'
          },{
              username: 'Alice',
              mobile: '15379316701',
              profession: '翻译',
              strength: '生成类',
              dislike: '',
              ability_score: '90'
          },{
              username: 'Alice',
              mobile: '15379316701',
              profession: '翻译',
              strength: '生成类',
              dislike: '',
              ability_score: '90'
          },{
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
            memory: '16G',
            vram: '2G',
            disk: '512G'
        },{
            ip: '192.168.0.1:8000',
            cpu: 'Intel Core i5-8500',
            gpu: 'NVIDIA GTX1080Ti',
            memory: '16G',
            vram: '2G',
            disk: '512G'
        },{
            ip: '192.168.0.1:8000',
            cpu: 'Intel(R) Core(TM) i5-8500',
            gpu: 'NVIDIA GTX1080Ti',
            memory: '16G',
            vram: '2G',
            disk: '512G'
        },{
            ip: '192.168.0.1:8000',
            cpu: 'Intel(R) Core(TM) i5-8500',
            gpu: 'NVIDIA GTX1080Ti',
            memory: '16G',
            vram: '2G',
            disk: '512G'
        },{
            ip: '192.168.0.1:8000',
            cpu: 'Intel Core i5-8500',
            gpu: 'NVIDIA GTX1080Ti',
            memory: '16G',
            vram: '2G',
            disk: '512G'
        },{
            ip: '192.168.0.1:8000',
            cpu: 'Intel Core i5-8500',
            gpu: 'NVIDIA GTX1080Ti',
            memory: '16G',
            vram: '2G',
            disk: '512G'
        },{
            ip: '192.168.0.1:8000',
            cpu: 'Intel Core i5-8500',
            gpu: 'NVIDIA GTX1080Ti',
            memory: '16G',
            vram: '2G',
            disk: '512G'
        }],
        addHumanDialog: false,
        form: {
          name: '',
          mobile: '',
          profession: '',
          type: []
        },
        addMachineDialog: false,
        mform: {
          ip: '',
          cpu: '',
          gpu: '',
          resource: ''
        }
      }
  },
  methods: {
    checkHumanDetail () {
      this.$router.push('/humanDetail')
    }
  }
}
</script>

<style>
.personIcon {
    width: 40px;
    height: 40px
}
.el-table {
    margin-top: 10px;
}
.addButton {
    margin-left: 480px;
    margin-top: 10px;
}
</style>