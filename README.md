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

> a. Create two connections for managing the two databases.

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/07.png" width="280px" height="200px" />    
<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/08.png" width="260px" height="260px" />      

> b. Execute SQL files in the databases to verify the successful connection.

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/09.png" width="250px" height="300px" />  

### 3. Launch the hmOS_V1.0 project.

**(1) Initiate the frontend interface using the command: 'npm run dev'.** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/10.png" width="290px" height="100px" />   

**Upon successful initiation:** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/11.png" width="400px" height="156px" />  

**(2) Launch the backend tasks by navigating to the 'server' folder and executing the command: 'node app.js'.** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/12.png" width="600px" height="130px" />   

**(3) Open a new PowerShell window within the 'aliOSS' folder and run the command: 'node app.js'.** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/13.png" width="500px" height="62px" />   

**(4) Perform user login through the frontend initiated in the first step.** 

### 4. Execute the pedestrian re-identification task.

**(1) Upon logging in, access the platform homepage and utilize the "Create Task" function to initiate a task.** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/14.png" width="700px" height="350px" />   

**(2) Create a pedestrian re-identification task by selecting the "identification" category.** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/15.png" width="700px" height="350px" />   

**(3) Input task details such as Name, Time Limit, Accuracy Limit, and Description, then proceed by clicking the "NEXT" button.** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/16.png" width="700px" height="350px" />   

**(4) Within the Dataset section, perform the "Select" button on the target objects for recognition tasks, followed by the "Upload" button for the associated videos. Upon completion, click the "Finished" button.** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/17.png" width="700px" height="350px" />     

**(5) Utilize the "Task View" function on the homepage to monitor the progress of tasks.** 

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/18.png" width="700px" height="350px" />    

**(6) During task execution, click the right-sided red box (which turns yellow when in progress) to initiate sampling, assigning photos for human annotation.**

<img src="https://github.com/hmOS-team-project/hmOS_V1.0/blob/master/IMG/19.png" width="700px" height="350px" />   
