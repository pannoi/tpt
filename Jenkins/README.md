# Jenkins

## Инфо

Jenkins - программная система с открытым исходным кодом на Java, предназначенная для обеспечения процесса непрерывной интеграции программного обеспечения.
Непрерывная интеграция- это процесс разработки программного обеспечения, смысл которого заключается в постоянном соединении рабочих копий в общую линию разработки, и выполнении постоянных автоматизированных сборок проекта для быстрого выявления возможных ошибок и решения интеграционных проблем.

Для того, чтобы связать Jenkins с GitHub репозиторием, необходимо выполнить следующие действия:

## Установка Jenkins
> Windows

Дла того, чтобы установить Jenkins на Windows, нужно скачать установочный файл с официального сайта.
> https://www.jenkins.io/download/



## Установка плагинов
Для установки необходимых плагинов необходимо пройти в:
Manage Jenkins > Manage Plugins > Availabe

Перед вами появляется список доступных для установки плагинов
![Image of collaborator](https://github.com/pannoi/tpt/blob/master/Jenkins/images/PluginsListJenkins.PNG)

Для корректной работы с Git убедитесь, что у вас установлен Git на компьютер, а так же установлены следующие плагины в Jenkins:
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

> Так же для работы, нам понадобятся плагины:
```bash
Blue Ocean
#BlueOcean Aggregator

Docker plugin
#This plugin integrates Jenkins with Docker
```
## Создание проекта
Для создания проекта в Jenkins, на главной станице пройдите в:
```bash
New Item > Укажите имя и выберите тип Pipeline, после чего снизу нажимаем OK
```
![Image of collaborator](https://github.com/pannoi/tpt/blob/master/Jenkins/images/CreateProjektJenkins.PNG)

После этого, ниже в разделе Pipeline, выбираем следующие параметры:
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

Для завершения нажимаем SAVE

> При возникновении ошибки, связанной с подключением к Git репозиторию, убедитесь что у вас указан путь к git.exe на вашем компьютере.
```bash
Failed to connect to repository :
Error performing git command: 
git.exe ls-remote -h https://github.com/username/projekt.git HEAD
```
Для настройки, нужно пройти в:
```bash
Manage Jenkins > Global Tool Configuration > Git
```
В поле Path to Git executable нужно указать путь до git.exe, установленном на вашем компьютере. 
> By Deffault - C:\Users\username\AppData\Local\Programs\Git\cmd\git.exe


## Билд проекта

Поле того как мы создали проект, он отобразится на главной странице в Jenkins
![Image of collaborator](https://github.com/pannoi/tpt/blob/master/Jenkins/images/ProjektOnMainPageJenkins.PNG)

Чтобы произвести билд проекта, нам нужно нажать на его название. В открывшемся окне проекта, нам необходимо нажать на кнопку [ Build Now ], которая находится в меню слева.
> P.s. Для проведения билда, нужно создать блок в файле Jenkinsfile, который должен храниться в ветке вашего приложения.

![Image of collaborator](https://github.com/pannoi/tpt/blob/master/Jenkins/images/ProjektBuildJenkins.PNG)

После успешного билда проекта, результат можно посмотреть, нажав [ Open Blue Ocean ] в меню слева.

![Image of collaborator](https://github.com/pannoi/tpt/blob/master/Jenkins/images/ProjektBuildResult.PNG)

Как можно видеть, билд прошел успешно

> Так же, при возникновении ошибок вам будет описано, в чем у вас заключается проблема.
