# Git

## Info

A version control system or VCS can make it much easier for developers trying to analyze changes and contributions to shared code. Simply said, the version control system is a key element in the software settings management system that meets the needs of the project. VCS allow you to assign letters or numerical values for certain changes/revisions/updates. You can also provide information about temporary labels and ID of the person who made the change.

> Read more here:
https://git-scm.com/book/ru/v2/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-Git

## Workflow

In Git, you can find general information about utilities and methods with examples that will be used in the keep up.

## Updating the repository by students

If you want to update something inside my repository, then click on fork and do a Pull Request to the master, after which I will check and can make merge and repository will update. Review and update of documentation is welcome.

![Image of pull request](https://github.com/pannoi/tpt/blob/master/git/images/pullRequest.png)

## Student repositories

Students should create a ```Private``` Repository, and then add me ```https://github.com/pannoi``` как collaborator.

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
