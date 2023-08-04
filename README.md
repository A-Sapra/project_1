# Project_1

Author - Aman Sapra

Objective - 
Create a python Flask app to be able to backup a file, connected to a MYQSL database and be able to display logs of the backup and a stat function to see how many backups as well as the number of failed and successful backups. 

# Project_2 - Jenkins (CI/CD), Docker, NEXUS

## Objective - 
Use Jenkins and Nexus to automate a CI pipline for the backup app built in project 1. It should be able to push new changes to the repository when changes are made to the source code.

The technologies that are to be used include:

-Kanban Board: Trello or an equivalent Kanban Board 
-Database: MySQL workbench
-Source code: Python and Flask for Python Web Development
-Version Control: Git 
-CI Server: Jenkins  
-Containerisation: Docker 
-Central repository :Nexus 

## The requirements of the project are as follows:

To use a Trello board (or equivalent Kanban board tech) with full expansion on user stories, use cases and tasks needed to complete the project. It could also provide a record of any issues or risks that you faced creating your project.
To use an inline relational database used to store data persistently for the project.
To provide clear Documentation from a design phase describing the architecture you will use for you project as well as a detailed Risk Assessment.
To deploy a containerised image of project 1's application stored in a nexus repository. A functioning API, using Flask.
For code to be fully integrated into a Version Control System using the Feature-Branch model which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
You should consider the concept of MVP (Minimum Viable Product) as you plan your project, completing all the requirements above before you add extra functionality that is not specified above.

## Tasks
Configure Nexus - initial setup of the programme

Configure Nexus for docker, you will need at a docker hosted repository and docker proxy repository

You will need to provision and set up a VM that can run your Jenkins Pipeline and also to host your Nexus Repository - this should be provided

Ensure that the application from project 1 runs in a container on the VM

You will use docker syntax to ensure that an image is generated that can be stored in the Nexus repo.

Be sure to demonstrate testing of your deployment to Nexus.

Create Jenkins Pipeline for automation - Jenkinsfile in the repo needs to be in the directory before the code. 

The previous tasks can be automated by Jenkins. Create a Jenkinsfile that will automate this process. Ensure that Jenkins is correctly connecting to the Nexus repository and has the correct permissions to use docker.

## Deliverables
The final deliverable for this project is a completed CI Pipeline with full documentation around the utilisation of supporting tools. Your documentation should also include evidence of design, risk assessment and testing.
The CI Pipeline needs to be able to successfully deploy the application you have created as per the requirements. Your pipeline should support fully automatic deployment of code updates in real time, including pushing the latest image to the nexus repository.
Your database should be an inline sqlite database in this case, successful connections to a database instance or sql container will not garner extra marks, though it would demonstrate a greater skillset.

# Plannnig

Database in MySQL workbench -

![image](https://github.com/A-Sapra/project_1/assets/139867167/a11eb849-fb3e-4617-93d5-702c8fdc4096)

Using Trello - 

![image](https://github.com/A-Sapra/project_1/assets/139867167/4fcda6ad-563c-4caf-97d0-3a9b815a4462)


# Risk assessment

![image](https://github.com/A-Sapra/project_1/assets/139867167/2e3550a0-c266-4348-b203-d6e32dc7f2d3)




# Steps -
Setup docker desktop and change docker engine to allow insecure registries
# Docker desktop 
![image](https://github.com/A-Sapra/project_1/assets/139867167/30e8568c-a67e-413e-8d4d-f892ac152530)
![image](https://github.com/A-Sapra/project_1/assets/139867167/9482a22b-0628-4dd3-a712-065444c4cd76)
![image](https://github.com/A-Sapra/project_1/assets/139867167/3cf903e6-ba9f-40fa-9d87-afb9ce370a23)

Use windows command line to use docker and download images
# Docker commands in windows command line - 
![image](https://github.com/A-Sapra/project_1/assets/139867167/e4cece58-7f21-42d1-9375-b9ac5f8aad39)
![image](https://github.com/A-Sapra/project_1/assets/139867167/408c0445-79f7-46ca-8b69-a2c7c3ab33ae)
![image](https://github.com/A-Sapra/project_1/assets/139867167/6d33d84d-2673-407e-a84a-7f62109fe9d1)
![image](https://github.com/A-Sapra/project_1/assets/139867167/12af8264-f119-4e87-8bad-69be9c37ccd3)
![image](https://github.com/A-Sapra/project_1/assets/139867167/9485d21a-2c6b-425c-9a06-689f23093c57)
![image](https://github.com/A-Sapra/project_1/assets/139867167/feb1819a-eaa1-4f7e-89e4-1a5511d0ff3a)
![image](https://github.com/A-Sapra/project_1/assets/139867167/74e081f9-e138-4b06-8b6e-ab00f412da87)
![image](https://github.com/A-Sapra/project_1/assets/139867167/fa9d7ad3-ace1-4cab-a6f2-aa93ebe4068c)
![image](https://github.com/A-Sapra/project_1/assets/139867167/4da45fe3-4d10-471f-876d-9d124eb41b3a)
![image](https://github.com/A-Sapra/project_1/assets/139867167/cf0e3907-0ba5-4c79-8e1e-e8d2d35cee3a)
![image](https://github.com/A-Sapra/project_1/assets/139867167/8d82d6d8-6f09-4acb-b601-fbf6067a579e)
![image](https://github.com/A-Sapra/project_1/assets/139867167/111f9b71-d9bc-4e8a-ab31-085f92dd264a)

Set up nexus repos 

# Nexus screenshots - 
Nexus credentials - 
username - admin
initial password - comes from command line when running the setup file
password - root
![image](https://github.com/A-Sapra/project_1/assets/139867167/f0c74ea0-8fb9-4032-a655-e070bdfb4985)
![image](https://github.com/A-Sapra/project_1/assets/139867167/743d31c0-e7c9-4476-8a88-4d59301dd092)
![image](https://github.com/A-Sapra/project_1/assets/139867167/1f21def8-3252-42ad-8375-9cd2d7ce115d)
![image](https://github.com/A-Sapra/project_1/assets/139867167/d3011b5c-3112-4b5f-9783-ee127222eca0)
![image](https://github.com/A-Sapra/project_1/assets/139867167/b013f51e-858c-410d-b805-74b2eecfa593)
![image](https://github.com/A-Sapra/project_1/assets/139867167/3a123420-598a-4079-a729-cdeb830eaa55)
![image](https://github.com/A-Sapra/project_1/assets/139867167/86ffcc51-b4b0-4b07-bd8a-91cbc401f156)

# Git Bash terminal -
![image](https://github.com/A-Sapra/project_1/assets/139867167/e5379ead-27dd-46f4-a44b-a04297304936)
![image](https://github.com/A-Sapra/project_1/assets/139867167/430afdbc-2b6e-48fb-935c-3bf441be1959)
![image](https://github.com/A-Sapra/project_1/assets/139867167/7e1c6b9c-1108-4c2d-a0f7-776ec56a69f7)
![image](https://github.com/A-Sapra/project_1/assets/139867167/b3e2edf2-d0d2-4a9a-b60e-100b4c0fe0e2)

# Docker file -
![image](https://github.com/A-Sapra/project_1/assets/139867167/ce0f0a11-b45a-4356-9b84-833c1e7d1a06)

# Windows command line - wsl to make linux work in command line 
![image](https://github.com/A-Sapra/project_1/assets/139867167/d597c429-3fe2-4fe1-8a13-557881f7b48f)
![image](https://github.com/A-Sapra/project_1/assets/139867167/9a7b1230-5ccf-4df9-9180-181035cbdc16)
![image](https://github.com/A-Sapra/project_1/assets/139867167/6c8295ef-e137-4bf4-91c2-77b20979edb4)
![image](https://github.com/A-Sapra/project_1/assets/139867167/7880af8b-07b0-4fe8-af81-2853c164cd3b)
![image](https://github.com/A-Sapra/project_1/assets/139867167/1d0c651d-fed3-4e72-8af9-98b2539b4136)

# MySQL workbench -

![image](https://github.com/A-Sapra/project_1/assets/139867167/d794c452-4303-43cf-aa5c-9ed62240ddfc)

# Jenkins screenshots - 
jenkins credentials - 
username - AS
password - root
![image](https://github.com/A-Sapra/project_1/assets/139867167/d0b500c0-b970-4796-ba95-b8bf7cce696c)
![image](https://github.com/A-Sapra/project_1/assets/139867167/2798cf5b-e86d-4b18-8cc2-9c13667a9c41)
![image](https://github.com/A-Sapra/project_1/assets/139867167/4969b287-c5ed-4003-8bb8-ec3939a9e38b)
![image](https://github.com/A-Sapra/project_1/assets/139867167/ab438741-b75c-43a3-861d-9fd9552cf9c1)
![image](https://github.com/A-Sapra/project_1/assets/139867167/6481fbfb-a4ba-4a4e-b439-688a5d4818b9)

actual jenkins file - 
![image](https://github.com/A-Sapra/project_1/assets/139867167/a80aa2c5-68cc-4895-8e09-7424776659cd)

running jenkins builds
![image](https://github.com/A-Sapra/project_1/assets/139867167/b4256436-bde7-4a1c-9502-f345c9ad4241)

console output -
![image](https://github.com/A-Sapra/project_1/assets/139867167/8060dd58-ed6f-4cf2-a19f-3fb05da94440)
![image](https://github.com/A-Sapra/project_1/assets/139867167/daf35e83-4bc1-423a-b3fa-904916eae1e6)
![image](https://github.com/A-Sapra/project_1/assets/139867167/4e8031d8-5d36-495f-8009-6ca95a6c9cdc)
![image](https://github.com/A-Sapra/project_1/assets/139867167/f359552a-bb00-46b3-8393-2af8d22a8ae3)
![image](https://github.com/A-Sapra/project_1/assets/139867167/c69cb686-5b2d-440c-9a2e-17519457597e)


Testing - 
![image](https://github.com/A-Sapra/project_1/assets/139867167/37711f83-96d0-489d-bd50-6051e2b9e245)
![image](https://github.com/A-Sapra/project_1/assets/139867167/05e8b38d-2a27-4a1d-800e-ff23a217816e)
![image](https://github.com/A-Sapra/project_1/assets/139867167/d56c0069-c8ed-4682-8003-71780c90d4ea)
![image](https://github.com/A-Sapra/project_1/assets/139867167/332fdbeb-7ebc-4938-bdb3-c6bd23121bf9)
![image](https://github.com/A-Sapra/project_1/assets/139867167/8286dbdb-3115-483a-bc53-24f2490977ea)
![image](https://github.com/A-Sapra/project_1/assets/139867167/8a2ebeb6-eac7-4469-9308-9358142adfaf)

































