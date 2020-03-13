# Git

## Инфо

Система контроля версий или VCS может значительно облегчить работу разработчиков, пытающихся проанализировать изменения и вклады в общий код. Проще говоря, система контроля версий — это ключевой элемент в системе управления настройками программного обеспечения, которые отвечают потребностям проекта. VCS дают возможность назначать для определенных изменений/ревизий/обновлений буквенные или числовые значения. Также могут предоставить информацию о временных метках и идентификаторе человека внесшего изменения. 

> Подробнее можете прочитать здесь:
https://git-scm.com/book/ru/v2/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-Git

## Workflow

В Git вы можете найти общую информацию по поводу утилит и методов с примерами которые будут использоваться в курсе.

## Обновление репозитория студентами

Если вы хотите что-то обновить внутри моего репозитория, то нажимаете на ```fork``` и далаете Pull Request в ```master```, после чего я проверю и могу сделать ```merge``` и репозиторий обновиться. Пересмотр и обновление документации приветсвуется.

![Image of pull request](https://github.com/pannoi/tpt/blob/master/git/images/pullRequest.png)

## Репозитории студентов

Студенты должны создать ```Private``` репозиторий, после чего сделать чего добавть меня ```https://github.com/pannoi``` как collaborator.

> Repository -> Settings -> Manage Access -> Invite collaborator -> @pannoi

![Image of collaborator](https://github.com/pannoi/tpt/blob/master/git/images/collaborators.PNG)

# Base commands

> In .gitignore you may specify files or folder, what you don't want to push in you repo, check exmaple in root directory in repository

```bash
# Clone whole repo from GIT 
git clone ${repo} ${path/to/folder}

# Pull latest changes from git to local branch
git pull

# Add changes to local branch, prepare for commit
git add .

# OR specific files
git add ${file}

# Commit changes
git commit -m "your message"

# Push changes to GIT 
git push

# Check status of current files comparing with GIT branch
git status

# Check difference between local branch and remote branch
git diff

# Check commit history 
git log

# Pull changes from specific branch or commit
git checkout ${branchName}
# OR
git checkout ${commitHash}
```
