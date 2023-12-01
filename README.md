# hmOS1.0 
## hmOS系统配置与运行  
### 一、克隆项目代码到本地
**（1）项目的github地址：<https://github.com/Miraclewyfei/hmOS1.0>**  

**（2）使用VScode将github中的项目代码进行克隆，具体如下：** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/01.png" width="700px" height="350px" />   

  
**（3）代码下载完成后，此时的文件夹如下：** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/02.png" width="250px" height="350px" />  
<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/03.png" width="250px" height="280px" />  
<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/04.png" width="250px" height="200px" />     
&emsp;&emsp;&emsp;&emsp;&emsp;项目文件&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;后端&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;前端&emsp; 

**（4）在VScode打开cmd，执行【npm install】（安装所需要的包）** 

### 二、配置数据库环境
**由于我们的hmOS存储用户的数据库是mysql，其在阿里云服务器上已经配置，无需配置；而存储任务的数据库是mongoDB，其在本地运行，需要在本地安装并配置mongoDB的环境。** 

**（1）在本地安装mongoDB**  

**（2）修改代码中配置mysql的文件，确保与阿里云服务器一致** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/05.png" width="250px" height="310px" />  
<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/06.png" width="450px" height="280px" />      

**（3）使用navicat软件可以测试数据库是否连接成功** 

> 1)新建两个连接，分别用于管理两个数据库

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/07.png" width="300px" height="210px" />   
<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/08.png" width="290px" height="280px" />     

> 2)在数据库中运行SQL文件，查看是否连接成功

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/09.png" width="250px" height="300px" />  

### 三、启动hmOS项目

**（1）启动前端界面，执行【npm  run dev】** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/10.png" width="290px" height="100px" />   

**启动成功后：** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/11.png" width="400px" height="156px" />  

**（2）启动任务后端（注意打开的文件夹server），执行【node app.js】** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/12.png" width="600px" height="130px" />   

**（3）再打开一个命令（注意文件夹为aliOSS）,执行【node app.js】** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/13.png" width="500px" height="62px" />   

**（4）可通过第一步启动的前端进行登录** 

### 四、执行行人重识别任务

**（1）注册登陆后，进入总控台界面，使用【Create Task】创建任务** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/14.png" width="700px" height="350px" />   

**（2）仅可以创建重识别任务，点击【identification】** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/15.png" width="700px" height="350px" />   

**（3）输入任务的Name、Time Limit、Accuracy Limit以及Description，点击【NEXT】（由于后端代码包装）** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/16.png" width="700px" height="350px" />   

**（4）在Dataset可对需要识别的target进行【Select】，之后对其【Upload】，并对视频进行上传，完成之后点击【Finished】** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/17.png" width="700px" height="350px" />     

**（5）可通过Task View对任务进行查看** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/18.png" width="700px" height="350px" />    

**（6）在任务的执行中，点击右边红色框（执行中会变成黄色），会进行采样，将照片交给human进行标记**

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/19.png" width="700px" height="350px" />   
