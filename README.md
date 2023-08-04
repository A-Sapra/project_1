# Project_1

Author - Aman Sapra

Objective - 
Create a python Flask app to be able to backup a file, connected to a MYQSL database and be able to display logs of the backup and a stat function to see how many backups as well as the number of failed and successful backups. 

# Project_2

Objective - 
Use Jenkins and Nexus to automate the build of the python flask app and be able to push new changes to the repository when changes are made to the source code.

The technologies that are to be used include:

-Kanban Board: Trello or an equivalent Kanban Board 
-MySQL workbench
-Version Control: Git 
-CI Server: Jenkins  
-Containerisation: Docker 
-Central repository :Nexus 

# Plannnig

Database in MySQL workbench -

![image](https://github.com/A-Sapra/project_1/assets/139867167/a11eb849-fb3e-4617-93d5-702c8fdc4096)


# Risk assessment


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

































