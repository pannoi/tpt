# Jenkins

## Info

Jenkins is an open source software system in Java designed to ensure the process of continuous software integration. Continuous integration is a software development process that involves constantly connecting work copies to a common development line, and executing permanent automated project builds to quickly identify possible errors and solve integration problems.

To link Jenkins to the GitHub repository, here's what you need to do:

## Jenkins Installation 
> Windows

To install Jenkins on Windows, you need to download the installation file from the official site.
> https://www.jenkins.io/download/



## Plugin Installation 
To install the necessary plug-ins, you need to go to: Manage Jenkins > Manage Plugins > Available

Here is a list of plug-ins available to install 
![Image of collaborator](https://github.com/pannoi/tpt/blob/master/Jenkins/images/PluginsListJenkins.PNG)

For proper work of GIT, make sure you have Git installed on your computer, as well as the following plugins in Jenkins:
```bash
Git client plugin
#Utility plugin for Git support in Jenkins	
	
Git Pipeline for Blue Ocean
#BlueOcean Git SCM pipeline creator

Git plugin
#This plugin integrates Git with Jenkins.
	
GIT server Plugin
#Allows Jenkins to act as a Git server.
	
GitHub API Plugin
#This plugin provides GitHub API for other plugins.
	
GitHub Branch Source Plugin
#Multibranch projects and organization folders from GitHub. Maintained by CloudBees, Inc.
	
GitHub Pipeline for Blue Ocean
#BlueOcean GitHub organization pipeline creator
	
GitHub plugin
#This plugin integrates GitHub to Jenkins.
```

> For wor as well you need next things:
```bash
Blue Ocean
#BlueOcean Aggregator

Docker plugin
#This plugin integrates Jenkins with Docker
```
## Project Creation
To create a project in Jenkins, on the main page, go to:
```bash
New Item > choose name and select type Pipeline, после чего снизу нажимаем OK
```
![Image of collaborator](https://github.com/pannoi/tpt/blob/master/Jenkins/images/CreateProjektJenkins.PNG)

After that, below in the Pipeline section, select the following options:
```bash
Definition > Pipeline script from CSM
 ```
 ```bash 
SCM > Git
 ```
  ```bash 
Repository URL > ссылка на ваш репозиторий на GitHub
 ```
![Image of collaborator](https://github.com/pannoi/tpt/blob/master/Jenkins/images/ConnectGitRepToProjekt.PNG)

To complete press SAVE

> If you have an error related to the Git repository connection, make sure you have a path to git.exe on your computer.
```bash
Failed to connect to repository :
Error performing git command: 
git.exe ls-remote -h https://github.com/username/projekt.git HEAD
```
To set up, you need to go to:
```bash
Manage Jenkins > Global Tool Configuration > Git
```
In the Path to Git executable field you need to point the way to git.exe installed on your computer.
> By Deffault - C:\Users\username\AppData\Local\Programs\Git\cmd\git.exe


## Project Build

After we create project, it will appear on the front page in Jenkins 
![Image of collaborator](https://github.com/pannoi/tpt/blob/master/Jenkins/images/ProjektOnMainPageJenkins.PNG)

To build a project, we need to click on its name. In the opening window of the project, we need to click on the "Build Now" button, which is on the menu on the left.
> P.s. To hold a build, you need to create a block in the Jenkinsfile file, which must be stored in the branch of your application.

![Image of collaborator](https://github.com/pannoi/tpt/blob/master/Jenkins/images/ProjektBuildJenkins.PNG)

After a successful project building, the result can be seen by clicking the [ Open Blue Ocean ] menu on the left.
![Image of collaborator](https://github.com/pannoi/tpt/blob/master/Jenkins/images/ProjektBuildResult.PNG)

As you can see, the build was made successfully

> Also, if you make mistakes, you'll be told what your problem is.
