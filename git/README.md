# Git

## Info

Versioonikontrollsüsteem või VCS võib teha palju lihtsamaks arendajad, kes üritavad analüüsida muudatusi ja panust ühiskasutusega koodi. Lihtsalt ütles, versioon kontrolli süsteem on võtmeelement tarkvara seadete juhtimissüsteemi, mis vastab projekti vajadustele. VCS võimaldab teil määrata tähed või numbrilised väärtused teatud muudatused/parandused/uuendused. Samuti saate anda teavet muudatuse teinud isiku ajutiste siltide ja ID kohta.

> Read more here:
https://git-scm.com/book/ru/v2/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-Git

## Workflow

Git, leiad üldine teave kommunaalteenuste ja meetodite näited tmüts  kasutatakse kursis.

## Updating the repository by students

Kui soovite värskendada midagi minu hoidla sees   ,  siis  klõpsa        kahvli ja tee pull taotluse Master, pärast mida ma kontrollin ja saab teha Merge ja hoidla uuendab. Dokumentatsiooni läbivaatamine ja uuendamine on teretulnud.

![Image of pull request](https://github.com/pannoi/tpt/blob/master/git/images/pullRequest.png)

## Student repositories

Õpilased peaksid looma Private Repository, ja  seejärel lisage mullehttps://github.com/pannoi as a collaborator.

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
