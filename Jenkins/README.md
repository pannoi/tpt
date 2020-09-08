# Jenkins

## Info

Jenkins on Java avatud lähtekoodiga Tarkvarakeskus, mille eesmärk on tagada pideva tarkvara integreerimise protsess. Pidev integratsioon on tarkvaraarendusprotsess, mis hõlmab pidevalt töökoopiate ühendamist ühisele arendusreale ja püsiva automatiseeritud projekti loomist, et kiiresti tuvastada võimalikke vigu ja lahendada integratsiooniprobleeme. Jenkinsi linkimiseks GitHub ' i hoidlaga peate tegema järgmist.



## Jenkins Installation
> Windows

Jenkins ' i installimiseks Windowsis peate installifaili alla laadima ametlikust saidilt.
> https://www.jenkins.io/download/



## Plugin Installation
Selleks, et installida vajalikud lisandmoodulid, peate minema:
Manage Jenkins > Manage Plugins > Availabe

Siin on loend lisandmoodulite installimiseks saadaval
![Image of collaborator](https://github.com/pannoi/tpt/blob/master/Jenkins/images/PluginsListJenkins.PNG)

Õige GITi tööks, veenduge, et teil on git arvutisse installitud, samuti ka järgmised pluginad Jenkins:
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

> Samuti tööks, on vaja plug-ins:
```bash
Blue Ocean
#BlueOcean Aggregator

Docker plugin
#This plugin integrates Jenkins with Docker
```
## Project Creation
Projekti loomiseks Jenkins ' is avalehel:
```bash
New Item > Vali nimi ja vali tüüp Pipeline, pärast seda vajuta OK
```
![Image of collaborator](https://github.com/pannoi/tpt/blob/master/Jenkins/images/CreateProjektJenkins.PNG)

Seejärel valige jaotises konveieri jaotis järgmised suvandid:
```bash
Definition > Pipeline script from CSM
 ```
 ```bash 
SCM > Git
 ```
  ```bash 
Repository URL > link  to your repository in GitHub
 ```
![Image of collaborator](https://github.com/pannoi/tpt/blob/master/Jenkins/images/ConnectGitRepToProjekt.PNG)

Vajutage SAVE

> Kui teil on tõrge, mis on seotud Git hoidla ühendus, veenduge, et teil on tee git. exe arvutis.
```bash
Failed to connect to repository :
Error performing git command: 
git.exe ls-remote -h https://github.com/username/projekt.git HEAD
```
Seadistamiseks peate minema:
```bash
Manage Jenkins > Global Tool Configuration > Git
```
Tee git käivitatava välja peate osutage tee git. exe arvutisse installitud. 
> By Deffault - C:\Users\username\AppData\Local\Programs\Git\cmd\git.exe


## Project Build


![Image of collaborator](https://github.com/pannoi/tpt/blob/master/Jenkins/images/ProjektOnMainPageJenkins.PNG)
Projekti koostamisekspeameklõpsama selle nimel. Projekti avamisaknas peame klõpsama nupul "ehitada nüüd", mis on vasakul menüüs.
> P.s. Ehitada, peate looma ploki Jenkinsfile faili, mis tuleb talletada oma taotluse haru.

![Image of collaborator](https://github.com/pannoi/tpt/blob/master/Jenkins/images/ProjektBuildJenkins.PNG)

Pärast edukat projektihoonet saab tulemust näha vasakul asuva menüü [ Open Blue Ocean ]klõpsamisega.

![Image of collaborator](https://github.com/pannoi/tpt/blob/master/Jenkins/images/ProjektBuildResult.PNG)

Nagu te näete , tehti b uILD  edukalttäielikult
