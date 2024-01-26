# hmOS_V1.0  
## hmOS V1.0 Platform Configuration and Deployment Process Instructions.  
### 1. Clone the project code to the local server.
**(1) The GitHub repository for the project can be found at：<https://github.com/hmOS-team-project/hmOS_V1.0>.**  

**(2) To clone the project code from GitHub, utilize VScode：** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/01.png" width="700px" height="350px" />     

  
**(3) Once the code download is complete, the folder structure will be as follows：** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/02.png" width="200px" height="330px" />   
<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/03.png" width="200px" height="250px" />   
<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/04.png" width="200px" height="180px" />    

&emsp;&emsp;&emsp;Project File&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Backend&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Frontend&emsp;   

**(4) Open the command prompt within VScode and execute "npm install" to install necessary dependencies.** 

### 2. Configure the backend database environment.
**Note: hmOS V1.0 platform utilizes mySQL for user database storage, configured on Alibaba Cloud Server, and mongoDB for task storage, requiring local installation and configuration of the mongoDB environment.** 

**(1) Install MongoDB on the local server.**  

**(2) Modify the MySQL configuration file in the code to ensure compatibility with the Alibaba Cloud server.** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/05.png" width="200px" height="280px" />   
<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/06.png" width="400px" height="240px" />       

**(3) Use Navicat software to test the database connection:** 

> 1) Create two connections for managing the two databases.

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/07.png" width="280px" height="200px" />    
<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/08.png" width="260px" height="260px" />      

> 2) Execute SQL files in the databases to verify the successful connection.

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/09.png" width="250px" height="300px" />  

### 3. Launch the hmOS_V1.0 project.

**（1）启动前端界面，执行【npm  run dev】:** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/10.png" width="290px" height="100px" />   

**启动成功后：** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/11.png" width="400px" height="156px" />  

**（2）启动任务后端（注意打开的文件夹server），执行【node app.js】:** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/12.png" width="600px" height="130px" />   

**（3）再打开一个命令（注意文件夹为aliOSS）,执行【node app.js】:** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/13.png" width="500px" height="62px" />   

**（4）可通过第一步启动的前端进行登录.** 

### 4. Execute the pedestrian re-identification task.

**（1）注册登陆后，进入总控台界面，使用【Create Task】创建任务:** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/14.png" width="700px" height="350px" />   

**（2）仅可以创建重识别任务，点击【identification】:** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/15.png" width="700px" height="350px" />   

**（3）输入任务的Name、Time Limit、Accuracy Limit以及Description，点击【NEXT】（由于后端代码包装）:** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/16.png" width="700px" height="350px" />   

**（4）在Dataset可对需要识别的target进行【Select】，之后对其【Upload】，并对视频进行上传，完成之后点击【Finished】:** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/17.png" width="700px" height="350px" />     

**（5）可通过Task View对任务进行查看:** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/18.png" width="700px" height="350px" />    

**（6）在任务的执行中，点击右边红色框（执行中会变成黄色），会进行采样，将照片交给human进行标记:**

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/19.png" width="700px" height="350px" />   
