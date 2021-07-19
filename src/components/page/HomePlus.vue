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
        <div class="flasheffectoutbox">
            <el-card
                :body-style="{ padding: '0px' }"
                shadow="hover"
                style="height: 600px; padding: 5px; background-color: rgba(1, 0, 191, 0.5); border: 0"
            >
                <div class="clearfix">
                    <img src="../../assets/img/external_collect.png" class="user-avator" alt />
                    <div class="resource-info-cont">System Function</div>
                    <el-input
                        placeholder="Please input function"
                        suffix-icon="el-icon-search"
                        class="search-box"
                        v-model="input2"
                        style="width: 200px; margin-left: 330px"
                    >
                    </el-input>
                </div>
                <!-- <hr style="border: 2 dashed #987cb9" SIZE="1" /> -->
                      <div class="divider div-transparent"></div>
                <div class="func-list">
                    <div class="func-list-box">
                        <div class="circleeffectclass aroundfunctioneffect" @click="tasktype()">
                            <img class="effectposition arounddataeffect02" src="@/assets/img/aroundeffect.png" />
                            <div class="effectposition acrossremindeffectout acrossremindeffectoutard">
                                <div class="acrossremindeffectin acrossremindeffectinard"></div>
                            </div>
                            <div style="padding: 18px">
                                <img
                                    class="effectposition acrossremindeffecindex"
                                    src="@/assets/img/createtask.png"
                                    width="38px"
                                    height="38px"
                                />
                            </div>
                            <span class="stagetitle stagearoundtitle">Create Task</span>
                        </div>
                    </div>
                    <div class="func-list-box">
                        <div class="circleeffectclass aroundfunctioneffect" @click="tasklist()">
                            <img class="effectposition arounddataeffect02" src="@/assets/img/aroundeffect.png" />
                            <div class="effectposition acrossremindeffectout acrossremindeffectoutard">
                                <div class="acrossremindeffectin acrossremindeffectinard"></div>
                            </div>
                            <div style="padding: 18px">
                                <img
                                    class="effectposition acrossremindeffecindex"
                                    src="@/assets/img/taskview.png"
                                    width="38px"
                                    height="38px"
                                />
                            </div>
                            <span class="stagetitle stagearoundtitle">Task View</span>
                        </div>
                    </div>
                    <div class="func-list-box">
                        <div class="circleeffectclass aroundfunctioneffect">
                            <img class="effectposition arounddataeffect02" src="@/assets/img/aroundeffect.png" />
                            <div class="effectposition acrossremindeffectout acrossremindeffectoutard">
                                <div class="acrossremindeffectin acrossremindeffectinard"></div>
                            </div>
                            <div style="padding: 18px">
                                <img
                                    class="effectposition acrossremindeffecindex"
                                    src="@/assets/img/mytasks.png"
                                    width="38px"
                                    height="38px"
                                />
                            </div>
                            <span class="stagetitle stagearoundtitle">My Task</span>
                        </div>
                    </div>
                    <div class="func-list-box">
                        <div class="circleeffectclass aroundfunctioneffect">
                            <img class="effectposition arounddataeffect02" src="@/assets/img/aroundeffect.png" />
                            <div class="effectposition acrossremindeffectout acrossremindeffectoutard">
                                <div class="acrossremindeffectin acrossremindeffectinard"></div>
                            </div>
                            <div style="padding: 18px">
                                <img
                                    class="effectposition acrossremindeffecindex"
                                    src="@/assets/img/mylist.png"
                                    width="38px"
                                    height="38px"
                                />
                            </div>
                            <span class="stagetitle stagearoundtitle">Task List</span>
                        </div>
                    </div>

                    <div class="func-list-box">
                        <div class="circleeffectclass aroundfunctioneffect">
                            <img class="effectposition arounddataeffect02" src="@/assets/img/aroundeffect.png" />
                            <div class="effectposition acrossremindeffectout acrossremindeffectoutard">
                                <div class="acrossremindeffectin acrossremindeffectinard"></div>
                            </div>
                            <div style="padding: 18px">
                                <img
                                    class="effectposition acrossremindeffecindex"
                                    src="@/assets/img/Settings.png"
                                    width="38px"
                                    height="38px"
                                />
                            </div>
                            <span class="stagetitle stagearoundtitle">Settings</span>
                        </div>
                    </div>
                    <div class="func-list-box">
                        <div class="circleeffectclass aroundfunctioneffect">
                            <img class="effectposition arounddataeffect02" src="@/assets/img/aroundeffect.png" />
                            <div class="effectposition acrossremindeffectout acrossremindeffectoutard">
                                <div class="acrossremindeffectin acrossremindeffectinard"></div>
                            </div>
                            <div style="padding: 18px">
                                <img
                                    class="effectposition acrossremindeffecindex"
                                    src="@/assets/img/Maintenance.png"
                                    width="38px"
                                    height="38px"
                                />
                            </div>
                            <span class="stagetitle stagearoundtitle">Maintenance</span>
                        </div>
                    </div>
                    <div class="func-list-box">
                        <div class="circleeffectclass aroundfunctioneffect" @click="inviteusers()">
                            <img class="effectposition arounddataeffect02" src="@/assets/img/aroundeffect.png" />
                            <div class="effectposition acrossremindeffectout acrossremindeffectoutard">
                                <div class="acrossremindeffectin acrossremindeffectinard"></div>
                            </div>
                            <div style="padding: 18px">
                                <img
                                    class="effectposition acrossremindeffecindex"
                                    src="@/assets/img/inviteuser.png"
                                    width="38px"
                                    height="38px"
                                />
                            </div>
                            <span class="stagetitle stagearoundtitle">User Invitation</span>
                        </div>
                    </div>
                    <div class="func-list-box">
                        <div class="circleeffectclass aroundfunctioneffect" >
                            <img class="effectposition arounddataeffect02" src="@/assets/img/aroundeffect.png" />
                            <div class="effectposition acrossremindeffectout acrossremindeffectoutard">
                                <div class="acrossremindeffectin acrossremindeffectinard"></div>
                            </div>
                            <div style="padding: 18px">
                                <img
                                    class="effectposition acrossremindeffecindex"
                                    src="@/assets/img/Application.png"
                                    width="38px"
                                    height="38px"
                                />
                            </div>
                            <span class="stagetitle stagearoundtitle">Application</span>
                        </div>
                    </div>
                    <div class="func-list-box">
                        <div class="circleeffectclass aroundfunctioneffect"@click="crowdsourcingaccess()">
                            <img class="effectposition arounddataeffect02" src="@/assets/img/aroundeffect.png" />
                            <div class="effectposition acrossremindeffectout acrossremindeffectoutard">
                                <div class="acrossremindeffectin acrossremindeffectinard"></div>
                            </div>
                            <div style="padding: 18px">
                                <img
                                    class="effectposition acrossremindeffecindex"
                                    src="@/assets/img/Crowdsourcing.png"
                                    width="38px"
                                    height="38px"
                                />
                            </div>
                            <span class="stagetitle stagearoundtitle">Crowdsourcing Access</span>
                        </div>
                    </div>
                    <div class="func-list-box">
                        <div class="circleeffectclass aroundfunctioneffect" @click="resourcemanagement()">
                            <img class="effectposition arounddataeffect02" src="@/assets/img/aroundeffect.png" />
                            <div class="effectposition acrossremindeffectout acrossremindeffectoutard">
                                <div class="acrossremindeffectin acrossremindeffectinard"></div>
                            </div>
                            <div style="padding: 18px">
                                <img
                                    class="effectposition acrossremindeffecindex"
                                    src="@/assets/img/Management.png"
                                    width="38px"
                                    height="38px"
                                />
                            </div>
                            <span class="stagetitle stagearoundtitle">Resource Management</span>
                        </div>
                    </div>
                </div>
            </el-card>
              <div class="copyrigntoutbox"><span class="copyrigntmsg">Copyright © 2021 Northwestern Polytechnical University All Rights Reserved</span></div>
            <!-- <div style="width: 1000px; height: 500px; position: relative">
           <div class="line2 line"></div>

                <div class="line3 line"></div>
                <div class="line4 line"></div>
                <div class="line5 line"></div>
                <div class="line6 line"></div> -->
            <!--主动效-->
            <!-- <div class="maineffectoutbox circleeffectclass" @click="gotocreate()">
                    <img class="effectposition maindataeffect" src="@/assets/img/maindataeffect.png" />
                    <div class="effectposition acrossremindeffectout" style="width: 76px; height: 76px; margin: 9px">
                        <div class="acrossremindeffectin" style="width: 68px; height: 68px; margin: 4px"></div>
                    </div>
                    <img class="effectposition maindataspecialeffect" src="@/assets/img/maindataspecialeffect.png" /><img
                        class="effectposition acrossremindeffecindex"
                        src="@/assets/img/maindataicon.png"
                    />
                    <span class="stagetitle">Create Task</span>
                </div> -->
            <!--卫星动效-->
            <!-- <div class="circleeffectclass aroundfunctioneffect" style="left: 254px; top: 135px">
                    <img class="effectposition arounddataeffect02" src="@/assets/img/aroundeffect.png" />
                    <div class="effectposition acrossremindeffectout acrossremindeffectoutard">
                        <div class="acrossremindeffectin acrossremindeffectinard"></div>
                    </div>
                    <img class="effectposition acrossremindeffecindex" src="@/assets/img/xingzhengshenpi.png" /><span
                        class="stagetitle stagearoundtitle"
                        >Task List</span
                    >
                </div>
                <div class="circleeffectclass aroundfunctioneffect" style="left: 189px; bottom: 89px">
                    <img class="effectposition arounddataeffect01" src="@/assets/img/aroundeffect.png" />
                    <div class="effectposition acrossremindeffectout acrossremindeffectoutard">
                        <div class="acrossremindeffectin acrossremindeffectinard"></div>
                    </div>
                    <img class="effectposition acrossremindeffecindex" src="@/assets/img/baixingpaiAPP.png" /><span
                        class="stagetitle stagearoundtitle"
                        >My List</span
                    >
                </div>
                <div class="circleeffectclass aroundfunctioneffect" style="right: 405px; bottom: 53px">
                    <img class="effectposition arounddataeffect02" src="@/assets/img/aroundeffect.png" />
                    <div class="effectposition acrossremindeffectout acrossremindeffectoutard">
                        <div class="acrossremindeffectin acrossremindeffectinard"></div>
                    </div>
                    <img class="effectposition acrossremindeffecindex" src="@/assets/img/zhatuyunshu.png" /><span
                        class="stagetitle stagearoundtitle"
                        >Resource Management</span
                    >
                </div>
                <div class="circleeffectclass aroundfunctioneffect" style="right: 243px; bottom: 165px">
                    <img class="effectposition arounddataeffect01" src="@/assets/img/aroundeffect.png" />
                    <div class="effectposition acrossremindeffectout acrossremindeffectoutard">
                        <div class="acrossremindeffectin acrossremindeffectinard"></div>
                    </div>
                    <img class="effectposition acrossremindeffecindex" src="@/assets/img/12319rexian.png" /><span
                        class="stagetitle stagearoundtitle"
                        >System Maintenance</span
                    >
                </div>
                <div class="circleeffectclass aroundfunctioneffect" style="right: 294px; top: 79px">
                    <img class="effectposition arounddataeffect03" src="@/assets/img/aroundeffect.png" />
                    <div class="effectposition acrossremindeffectout acrossremindeffectoutard">
                        <div class="acrossremindeffectin acrossremindeffectinard"></div>
                    </div>
                    <img class="effectposition acrossremindeffecindex" src="@/assets/img/zonghezhifa.png" /><span
                        class="stagetitle stagearoundtitle"
                        >Custom Application</span
                    >
                </div>
                <div class="circleeffectclass decarround01" style="top: 218px; left: 92px">
                    <div class="acrossremindeffectin decarroundin01" style=""></div>
                </div>
                <div class="circleeffectclass decarround01" style="top: 197px; right: 163px">
                    <div class="acrossremindeffectin decarroundin01" style=""></div>
                </div>
                <div class="circleeffectclass decarround02" style="top: 99px; right: 93px">
                    <div class="acrossremindeffectin decarroundin02" style=""></div>
                </div> 
            </div>-->
        </div>

        <!--侧边浮窗-->
        <div class="fltoutbox leftbox">
            <div style="height: 90px; padding-top: 35px"><span class="analyzedatashowtitle">【Personal Information】</span></div>
            <!--左上分析内容放置框-->
            <div class="analyzemsgbgbox" style="margin-left: 2px; height: 235px">
                <div style="display: flex; justify-content: space-around">
                    <div>
                        <img src="../../assets/img/img.jpg" class="user-avator" alt />
                    </div>
                    <div style="display: flex; flex-direction: column; justify-content: center; align-items: center">
                        <div style="color: white; font-weight: 500; font-size: 18px; margin-top: 10px">Hmc Group</div>
                        <div style="color: #aeaeae; font-weight: 400; font-size: 14px">hm@mail.nwpu.edu.cn</div>
                    </div>
                    <div style="display: flex; justify-content: center; align-items: center">
                        <el-dropdown class="user-name" trigger="click" @command="handleCommand">
                            <span class="el-dropdown-link">
                                <i class="el-icon-caret-bottom"></i>
                            </span>
                            <el-dropdown-menu slot="dropdown">
                                <a href="https://github.com/Miraclewyfei/hmOS1.0" target="_blank">
                                    <el-dropdown-item>My profile</el-dropdown-item>
                                </a>
                                <el-dropdown-item divided command="loginout">Log out</el-dropdown-item>
                            </el-dropdown-menu>
                        </el-dropdown>
                    </div>
                </div>
                <div>
                    <div style="margin: 18px 0px 4px 12px">
                        <div class="l_left" style="color: white; font-size: 14px; margin-right: 10px">Credit</div>
                        <div class="l_left" id="vaderSize0" style="width: 160px; padding: 0; margin-top: 4px"></div>
                        <div><span class="l_left" style="margin-left: 12px; color: #72ff00; font-size: 12px">80/100</span></div>
                        <div class="clear" style="margin-bottom: 10px"></div>
                        <div class="l_left" style="color: white; font-size: 14px; margin-right: 10px">Ability</div>
                        <div class="l_left" id="vaderSize00" style="width: 160px; padding: 0; margin-top: 4px"></div>
                        <div><span class="l_left" style="margin-left: 12px; color: #72ff00; font-size: 12px">60/100</span></div>
                        <div class="clear"></div>
                    </div>
                </div>
                <div class="divider div-transparent"></div>
                <div style="display: flex">
                    <div style="margin: 0 15px">
                        <div style="color: white">Released</div>
                        <div style="color: white; text-align: center">10</div>
                    </div>
                    <div style="margin: 0 15px">
                        <div style="color: white">Finished</div>
                        <div style="color: white; text-align: center">15</div>
                    </div>
                    <div style="margin: 0 15px">
                        <div style="color: white">Executing</div>
                        <div style="color: white; text-align: center">5</div>
                    </div>
                </div>
            </div>
            <!--左下分析内容放置框-->
            <div class="analyzemsgbgbox" style="margin-top: 20px; height: 350px; overflow: hidden">
                <span class="analyzedatashowtitle" style="line-height: 66px; margin-left: 20px">【Tasks Completed】</span>
                <div class="scrollbox">
                    <div id="scrollDiv">
                        <ul style="margin-top: -1.48947px">
                            <li>Car idea generation task <span style="">3/10</span></li>
                            <li>Finding Zhang task by the Public Security Department<span style="">3/10</span></li>
                            <li>Finding Li task by the Public Security Department<span style="">3/10</span></li>
                            <li>Finding Wang task by the Public Security Department<span style="">3/10</span></li>
                            <li>Fake news detection task of Public Security Department<span style="">3/10</span></li>
                            <li>Anomaly detection task of Public Security Department<span style="">3/10</span></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="fltdecarround fltdecarroundleft fltdecarroundtop"></div>
            <div class="fltdecarround fltdecarroundtop fltdecarroundright"></div>
            <div class="fltdecarround fltdecarroundleft fltdecarroundbottom"></div>
            <div class="fltdecarround fltdecarroundbottom fltdecarroundright"></div>
        </div>
        <div class="fltoutbox rightbox">
            <div style="height: 60px; padding-top: 25px">
                   <img  src="@/assets/img/humanunit.png" style="width:30px;height:30px;margin-left:10px"/>
                <span class="analyzedatashowtitle">【Human Unit】</span></div>
            <!--右上分析内容放置框-->
            <div class="analyzemsgbgbox" style="margin-right: 2px; padding-bottom: 29px; height: 250px">
                <div style="background-color: #022542; opacity: 0.9; height: 130px">
                    <div style="padding: 10px 0 0 16px">
                        <div class="l_left"><span style="color: #dfdede; font-size: 10px; margin-right: 10px">Crowds：</span></div>
                        <div class="l_left" id="vaderSize" style="width: 150px; padding: 0; margin-top: 6px">
                            <span class="barControl" style="width: 30%">
                                <!-- <div class="barContro_space"><span class="vader" style="height: 8px; overflow: hidden; width: 37.9969%;"
                  id="barvaderSize"></span></div> -->
                            </span>
                        </div>
                        <div class="l_left"><span style="color: #dd9809; margin-left: 4px; font-size: 10px">743人</span></div>
                        <div class="clear"></div>
                    </div>
                    <div style="padding: 8px 0 0 16px">
                        <div class="l_left"><span style="color: #dfdede; font-size: 10px; margin-right: 10px">Experts：</span></div>
                        <div class="l_left" id="vaderSize1" style="width: 150px; margin-top: 6px">
                            <span class="barControl" style="width: 30%">
                                <!-- <div class="barContro_space1"><span class="vader1" style="height: 8px; overflow: hidden; width: 27.9969%;"
                  id="barvaderSize1"></span></div> -->
                            </span>
                        </div>
                        <div class="l_left"><span style="color: #00d8ff; margin-left: 4px; font-size: 10px">216人</span></div>
                        <div class="clear"></div>
                    </div>
                    <div style="padding: 8px 0 0 16px">
                        <div class="l_left"><span style="color: #dfdede; font-size: 10px; margin-right: 6px">Persons：</span></div>
                        <div class="l_left" id="vaderSize2" style="width: 150px; margin-top: 6px">
                            <span class="barControl" style="width: 30%">
                                <!-- <div class="barContro_space2"><span class="vader2" style="height: 8px; overflow: hidden; width: 27.9969%;"
                  id="barvaderSize2"></span></div> -->
                            </span>
                        </div>
                        <div class="l_left"><span style="color: #56a4ff; margin-left: 4px; font-size: 10px">2037人</span></div>
                        <div class="clear"></div>
                    </div>
                    <div style="padding: 8px 0 0 16px">
                        <div class="l_left"><span style="color: #dfdede; font-size: 10px; margin-right: 10px">Others：</span></div>
                        <div class="l_left" id="vaderSize3" style="width: 150px; margin-top: 6px">
                            <span class="barControl" style="width: 30%">
                                <!-- <div class="barContro_space3"><span class="vader3" style="height: 8px; overflow: hidden; width: 27.9969%;"
                  id="barvaderSize3"></span></div> -->
                            </span>
                        </div>
                        <div class="l_left"><span style="color: #56ff6a; margin-left: 4px; font-size: 10px">651人</span></div>
                        <div class="clear"></div>
                    </div>
                </div>
                <div style="margin-top:15px">
                <img  src="@/assets/img/GPU.png" style="width:30px;height:30px;margin-left:10px"/>
                    <p style="color: #dfdede; font-size: 14px; margin: -25px 0 0 50px; font-weight: 700">【GPU Unit】</p>
                    <div class="l_left" id="vaderSize4" style="width: 200px; padding: 0; margin: 40px 0 0 18px">
                        <span class="barControl" style="width: 30%">
                            <!-- <div class="barContro_space4"><span class="vader4" style="height: 22px; overflow: hidden; width: 55.9939%;"
                id="barvaderSize4"></span></div> -->
                        </span>
                    </div>

                    <div class="l_left" style="color: #ffea00; margin: 44px 0 0 4px; font-size: 14px"><span>200/413</span></div>
                </div>
                <div class="fltdecarround fltdecarroundleft fltdecarroundbottom"></div>
                <div class="fltdecarround fltdecarroundbottom fltdecarroundright"></div>
            </div>
            <!--右下分析内容放置框-->
            <div class="analyzemsgbgbox" style="margin-top: 20px; height: 365px">
                <span class="analyzedatashowtitle">【Task Progress】</span>
                <div style="margin: 0 6px; background-color: #011c2f; opacity: 0.8; padding: 8px 0 6px 0">
                    <div>
                        <div><span class="down_span">【Task One】</span></div>
                        <div style="margin: 5px 0 4px 12px">
                            <div class="l_left" id="vaderSize5" style="width: 190px; padding: 0; margin-top: 4px">
                                <span class="barControl" style="width: 30%">
                                    <!-- <div class="barContro_space5"><span class="vader5"
                    style="height: 8px; overflow: hidden; width: 14.9317%;" id="barvaderSize5"></span></div> -->
                                </span>
                            </div>

                            <div><span class="l_left" style="margin-left: 12px; color: #40e315; font-size: 12px">8.02%</span></div>
                            <div class="clear"></div>
                        </div>
                        <div><span class="down_span">【Task Two】</span></div>
                        <div style="margin: 5px 0 4px 12px">
                            <div class="l_left" id="vaderSize6" style="width: 190px; padding: 0; margin-top: 4px">
                                <span class="barControl" style="width: 30%">
                                    <!-- <div class="barContro_space6"><span class="vader6"
                    style="height: 8px; overflow: hidden; width: 14.9317%;" id="barvaderSize6"></span></div> -->
                                </span>
                            </div>

                            <div><span class="l_left" style="margin-left: 12px; color: #15e3ac; font-size: 12px">8.09%</span></div>
                            <div class="clear"></div>
                        </div>
                        <div><span class="down_span">【Task Three】</span></div>
                        <div style="margin: 5px 0 4px 12px">
                            <div class="l_left" id="vaderSize7" style="width: 190px; padding: 0; margin-top: 4px">
                                <span class="barControl" style="width: 30%">
                                    <!-- <div class="barContro_space7"><span class="vader7"
                    style="height: 8px; overflow: hidden; width: 5.59939%;" id="barvaderSize7"></span></div> -->
                                </span>
                            </div>

                            <div>
                                <span class="down_span l_left" style="margin-left: 12px; color: #1f9cff; font-size: 12px">2.87%</span>
                            </div>
                            <div class="clear"></div>
                        </div>
                        <div><span class="down_span">【Task Four】</span></div>
                        <div style="margin: 5px 0 4px 12px">
                            <div class="l_left" id="vaderSize8" style="width: 190px; padding: 0; margin-top: 4px">
                                <span class="barControl" style="width: 30%">
                                    <!-- <div class="barContro_space8"><span class="vader8"
                    style="height: 8px; overflow: hidden; width: 1.86646%;" id="barvaderSize8"></span></div> -->
                                </span>
                            </div>

                            <div>
                                <span class="down_span l_left" style="margin-left: 12px; color: #c97802; font-size: 12px">0.85%</span>
                            </div>
                            <div class="clear"></div>
                        </div>
                        <div><span class="down_span">【Task Five】</span></div>
                        <div style="margin: 5px 0 4px 12px">
                            <div class="l_left" id="vaderSize9" style="width: 190px; padding: 0; margin-top: 4px">
                                <span class="barControl" style="width: 30%">
                                    <!-- <div class="barContro_space9"><span class="vader9"
                    style="height: 8px; overflow: hidden; width: 77.4582%;" id="barvaderSize9"></span></div> -->
                                </span>
                            </div>

                            <div><span class="l_left" style="margin-left: 12px; color: #72ff00; font-size: 12px">80.44%</span></div>
                            <div class="clear"></div>
                        </div>
                        <div><span class="down_span">【Task Six】</span></div>
                        <div style="margin: 5px 0 4px 12px">
                            <div class="l_left" id="vaderSize10" style="width: 190px; padding: 0; margin-top: 4px">
                                <span class="barControl" style="width: 30%">
                                    <!-- <div class="barContro_space10"><span class="vader10"
                    style="height: 8px; overflow: hidden; width: 5.59939%;" id="barvaderSize10"></span></div> -->
                                </span>
                            </div>
                            <div><span class="l_left" style="margin-left: 12px; color: #ef4503; font-size: 12px">2.56%</span></div>
                            <div class="clear"></div>
                        </div>
                    </div>
                </div>
                <div class="fltdecarround fltdecarroundleft fltdecarroundtop"></div>
                <div class="fltdecarround fltdecarroundtop fltdecarroundright"></div>
                <div class="fltdecarround fltdecarroundleft fltdecarroundbottom"></div>
                <div class="fltdecarround fltdecarroundbottom fltdecarroundright"></div>
            </div>
        </div>
    </div>
</template>
<script>
import '@/assets/css/Datacages_Homeindex.css';
import '@/assets/css/ProgressBarWars.css';
import '@/assets/js/jquery.min.js.下载';
import '@/assets/js/echarts-all.js.下载';
import '@/assets/js/ProgressBarWars.js.下载';

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
         tasktype(){
                 this.$router.push('/tasktypeplus');
        },
        tasklist(){
                 this.$router.push('/tasklistplus');
        },
        mytask(){
                 this.$router.push('/mytask');
        },
        resourcemanagement(){
            this.$router.push('/resourcemanagementplus')
        },
        crowdsourcingaccess(){
            this.$router.push('/crowdsourcingaccess')
        },
        inviteusers(){
            this.$router.push('/inviteusers')
        }
    },
    mounted() {
        window.onload = function () {
            var loading = document.getElementById('loading');
            loading.style.display = 'none';
        };
        $('#vaderSize10').ProgressBarWars10({
            porcentaje: 6,
            estilo: 'vader10',
            tiempo: 5980,
            alto: '8px',
            flag: true
        });

        $('#vaderSize9').ProgressBarWars9({
            porcentaje: 83,
            estilo: 'vader9',
            tiempo: 5980,
            alto: '8px',
            flag: true
        });
        $('#vaderSize0').ProgressBarWars9({
            porcentaje: 80,
            estilo: 'vader9',
            tiempo: 5980,
            alto: '8px',
            flag: true
        });
        $('#vaderSize00').ProgressBarWars9({
            porcentaje: 60,
            estilo: 'vader9',
            tiempo: 5980,
            alto: '8px',
            flag: true
        });
        $('#vaderSize8').ProgressBarWars8({
            porcentaje: 2,
            estilo: 'vader8',
            tiempo: 5980,
            alto: '8px',
            flag: true
        });
        $('#vaderSize7').ProgressBarWars7({
            porcentaje: 6,
            estilo: 'vader7',
            tiempo: 5980,
            alto: '8px',
            flag: true
        });
        $('#vaderSize6').ProgressBarWars6({
            porcentaje: 16,
            estilo: 'vader6',
            tiempo: 5980,
            alto: '8px',
            flag: true
        });
        $('#vaderSize5').ProgressBarWars5({
            porcentaje: 16,
            estilo: 'vader5',
            tiempo: 5980,
            alto: '8px',
            flag: true
        });
        var number = 60;
        $(function () {
            console.log();
            $('#vaderSize4').ProgressBarWars4({
                porcentaje: number,
                estilo: 'vader4',
                tiempo: 5980,
                alto: '22px',
                flag: true
            });
            setInterval(function () {
                number = Math.floor(Math.random() * 99 + 1);
                $('#vaderSize4').ProgressBarWars4({
                    porcentaje: number,
                    estilo: 'vader4',
                    tiempo: 5980,
                    alto: '22px',
                    flag: false
                });
            }, 5000);
        });
        var number = 90;
        $(function () {
            $('#vaderSize3').ProgressBarWars3({
                porcentaje: 30,
                estilo: 'vader3',
                tiempo: 5980,
                alto: '8px',
                flag: true
            });
            setInterval(function () {
                number = Math.floor(Math.random() * 99 + 1);
                $('#vaderSize3').ProgressBarWars3({
                    porcentaje: number,
                    estilo: 'vader3',
                    tiempo: 5980,
                    alto: '8px',
                    flag: false
                });
            }, 5000);
        });
        var number = 60;
        $(function () {
            $('#vaderSize2').ProgressBarWars2({
                porcentaje: 30,
                estilo: 'vader2',
                tiempo: 5980,
                alto: '8px',
                flag: true
            });
            setInterval(function () {
                number = Math.floor(Math.random() * 99 + 1);
                $('#vaderSize2').ProgressBarWars2({
                    porcentaje: 20,
                    estilo: 'vader2',
                    tiempo: 5980,
                    alto: '30px',
                    flag: false
                });
            }, 5000);
        });
        $(function () {
            $('#vaderSize1').ProgressBarWars1({
                porcentaje: 30,
                estilo: 'vader1',
                tiempo: 5980,
                alto: '8px',
                flag: true
            });
            setInterval(function () {
                number = Math.floor(Math.random() * 99 + 1);
                $('#vaderSize1').ProgressBarWars1({
                    porcentaje: 90,
                    estilo: 'vader1',
                    tiempo: 5980,
                    alto: '30px',
                    flag: false
                });
            }, 5000);
        });
        $(function () {
            $('#vaderSize').ProgressBarWars({
                porcentaje: 30,
                estilo: 'vader',
                tiempo: 5980,
                alto: '8px',
                flag: true
            });
            setInterval(function () {
                number = Math.floor(Math.random() * 99 + 1);
                $('#vaderSize').ProgressBarWars({
                    porcentaje: 30,
                    estilo: 'vader',
                    tiempo: 5980,
                    alto: '30px',
                    flag: false
                });
            }, 5000);
        });
        $('#scrollDiv').Scroll({
            line: 1,
            speed: 500,
            timer: 5000,
            up: 'but_up',
            down: 'but_down'
        });
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

.scrollbox {
    width: 268px;
    margin: 0 auto;
}

#scrollDiv {
    width: 268px;
    height: 280px;
    overflow: hidden;
}

/*这里的高度和超出隐藏是必须的*/
#scrollDiv ul li {
    height: 66px;
    width: 259px;
    background-color: #07325e;
    overflow: hidden;
    margin-bottom: 4px;
    color: #dfdede;
    font-size: 14px;
    padding: 0 9px 0 9px;
    line-height: 30px;
    position: relative;
}

#scrollDiv ul li span {
    position: absolute;
    bottom: 5px;
    right: 16px;
    display: block;
    width: 68px;
    height: 18px;
    text-align: center;
    color: #081e49;
    background-color: #69c200;
    line-height: 18px;
}

.sent-div {
    width: 98%;
    height: 98%;
    margin: 0 auto;
}
.user-avator {
    width: 70px;
    height: 70px;
    border-radius: 50%;
}
.divider {
    position: relative;
    margin-top: 15px;
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
    background: url('../../assets/img/background1.png') no-repeat;
    background-size: 100% 100%;
    display: flex;
    align-items: center;
    padding: 10px;
    padding-right: 0px;
    border-bottom: 2px solid #ccc;
}

.user-avator {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    cursor: pointer;
}

.user-info-cont {
    width: 80px;
    height: 80px;
    background: url('../../assets/img/star-six.png') no-repeat;
    background-size: 100% 100%;
    font-size: 14px;
    color: white;
    margin-left: 50px;
    padding-top: 10px;
    text-align: center;
}

.user-info-cont div:first-child {
    font-size: 22px;
    color: #222;
    cursor: pointer;
}

.user-info-list {
    font-size: 14px;
    color: #999;
    line-height: 20px;
}

.user-info-list span {
    margin-left: 70px;
}

.mgb20 {
    margin-bottom: 20px;
    padding: 0px;
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
    float: left;
    margin-left: 80px;
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
    width: 20px;
    height: 40px;
    left: 0;
    top: 0;
    opacity: 0;
    cursor: pointer;
}
.upload-demo {
    width: 360px;
    float: left;
}
.query_input {
    margin-left: 360px;
}
.crop-btn-box {
    margin-top: 18px;
    float: right;
}
.task-submit-box {
    margin-left: 150px;
}
.information {
    margin-left: auto;
    height: 65px;
    width: 130px;
    line-height: 60px;
    background-color: pink;
    text-align: center;
    font-size: 22px;
    font-weight: 1000;
    border-radius: 50px;
    cursor: pointer;
}
.user-func {
    padding: 15px;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 180px;
    background-color: #d8d8d8;
}
.user-func-box {
    cursor: pointer;
}

.user-func-name {
    text-align: center;
    font-size: 18px;
    font-weight: 800;
}
.resource-info-cont {
    color: rgb(255, 255, 255);
    margin-left: 20px;
    font-size: 25px;
    font-weight: 300;
    cursor: pointer;
}
.resource-info {
    background: linear-gradient(to right, rgba(255, 0, 0, 0), rgb(3, 102, 11));
    /* background: linear, left top, left bottom, color-stop(0, #ff4f02), color-stop(1, #8f2c00); */
    display: flex;
    align-items: center;
    padding: 10px;
    padding-right: 0px;
    border-bottom: 2px solid #ccc;
}
.clearfix {
    display: flex;
    align-items: center;
}
.func-list {
    display: flex;
    flex-wrap: wrap;
}
.func-list-box {
    height: 100px;
    width: 80px;
    margin: 20px 70px 20px 60px;
}
.func-list-icon {
    width: 80px;
    height: 80px;
    cursor: pointer;
}
.func-list-name {
    cursor: pointer;
}
.search-box >>> .el-input__inner {
    background-color: rgba(0, 168, 255, 0.2);
    border: rgb(0, 228, 255);
}
</style>