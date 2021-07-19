<template>
    <div>
        <el-row :gutter="15">
          <el-col :span="6">
              <el-card>
                  <el-col :span="2" :gutter="20" class="personIconList"><el-row><img src="../../assets/img/circle.png" class="personIcon"/></el-row></el-col>
                  <el-col :span="4" :gutter="20" class="personMes">
                      <el-row>xing:Alice</el-row>
                      <el-row>Phone:15379316702</el-row>
                  </el-col>
              </el-card>
          </el-col>
          <el-col :span="6">
              <el-card>
                  <el-col :span="2" :gutter="20" class="personIconList"><el-row><img src="../../assets/img/taskIcon.png" class="taskIcon"/></el-row></el-col>
                  <el-col :span="4" :gutter="20" class="personMes">
                      <el-row>Count:1</el-row>
                      <el-row>In&nbsp;execution</el-row>
                  </el-col>
              </el-card>
          </el-col>
          <el-col :span="6">
              <el-card>
                  <el-col :span="2" :gutter="20" class="personIconList"><el-row><img src="../../assets/img/taskIcon.png" class="taskIcon"/></el-row></el-col>
                  <el-col :span="4" :gutter="20" class="personMes">
                      <el-row>Count:2</el-row>
                      <el-row>To&nbsp;be&nbsp;implemented</el-row>
                  </el-col>
              </el-card>
          </el-col>
          <el-col :span="6">
              <el-card>
                  <el-col :span="2" :gutter="20" class="personIconList"><el-row><img src="../../assets/img/taskIcon.png" class="taskIcon"/></el-row></el-col>
                  <el-col :span="4" :gutter="20" class="personMes">
                      <el-row>Count:10</el-row>
                      <el-row>Have&nbsp;finished&nbsp;tasks</el-row>
                  </el-col>
              </el-card>
          </el-col>
        </el-row>
        <el-row :gutter="15">
          <el-col :span="9">
              <el-card>
                  <template>
                    <el-table :data="humanData" stripe style="width: 100%">
                      <el-table-column prop="Profession" label="Profession" width="180"></el-table-column>
                      <el-table-column prop="State" label="State" width="180"></el-table-column>
                      <el-table-column prop="Ability_score" label="Ability-score"></el-table-column>
                      <el-table-column prop="Strength" label="Strength"></el-table-column>
                      <el-table-column prop="Dislike" label="Dislike"></el-table-column>
                    </el-table>
                  </template>
              </el-card>
          </el-col>
          <el-col :span="15">
              <el-card></el-card>
          </el-col>
        </el-row>
    </div>
</template>

<script>
export default {
    data () {
        return {
            humanData: [
                {
                    Profession: 'Translator',
                    State: 'Online',
                    Ability_score: '',
                    Strength: 'Generation',
                    Dislike: 'Recognization'
                }
            ]
        }
    }
}
</script>

<style>
.personIcon {
    width: 80px;
    height: 80px;
}

.taskIcon {
    width: 80px;
    height: 80px;
}

.el-col {
    border-radius: 4px;
}

 .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }

.personIconList {
    margin-right: 70px;
    margin-bottom: 20px;
}

.personMes {
    margin-top: 20px;
}
</style>