# GIT CHEATSHEET

## Questions
- what about forking?
- why would you fetch instead of pull?
- difference between git and git-all package?
- Note: try pandoc for my website

## initialization
```bash
git init
git config --add --global user.name "francistops"
git config --add --global user.email "65456051+francistops@users.noreply.github.com"
git config --global init.defaultBranch main
git config --global pull.rebase true
git config --global --add --bool push.autoSetupRemote true
```

## Solo Workflow
```bash
git add .
git commit
git push origin main
git pull origin main

git log --oneline
git reset --soft HEAD~1
```
## Collaborative Workflow
```bash
pull origin main
git switch -c "branchname"
git add .
git commit
git push origin "branchname"
```
- Open a pull request on GitHub to merge my changes into main
- waiting to be review and merge to main
- Delete my feature branch

## Installation
`sudo apt install git`\
`sudo apt install git-all`

## Configuration
### Configuration Location
- system: /etc/gitconfig          # system global
- global: ~/.gitconfig            # user global
- local: .git/config              # project specific
- worktree: .git/config.worktree  # part of project

### Configuration Command
```bash
git config --add --global user.name "francistops"
git config --add --global user.email "65456051+francistops@users.noreply.github.com"
git config --global init.defaultBranch main
git config --global pull.rebase true
git config --list --local
git config --get <section>.<key>
git config --unset <key>
git config --remove-section <section>
```
## Porcelaine Command
```bash
git init
git add < . or file(s) > 
git rm < . or file(s) > 
git status
git commit --amend -m ""

git log --oneline
git log --oneline --graph --all
git log --oneline --decorate --graph --parents
git log -n 10 --decorate=full
git log remote/branch

git branch
git branch -m "oldname" "newname"
# git switch = git checkout
git switch -c my_new_branch [COMMITHASH]
git branch -d "branchname"

git merge "branchname"  # from main branch
git merge origin/main
# resolve merge conflic by editing the file in conflic then commit or remove it
git rebase main         # from feature branch

git reset --soft HEAD~1     # keep changes
git reset --hard COMMITHASH # Danger changes made after COMMITHASH are lost.

git remote add <name> <uri>
git remote rename "oldname" "newname"
git remote -v
git remote add origin git@github.com:francistops/webflyx.git
git ls-remote

git fetch # fetch objects not files
git pull origin main

git push origin main
git push origin "localbranch" "remotebranch"
git push origin :"remotebranch" # delete remotebranch
```
## Github-CLI

### Installation
`curl -sS https://webi.sh/gh | sh`

### Authentification
`gh auth login # ssh is prefered`

### Adding Github Repo
- create a repo on github
  
`git remote add origin git@github.com:francistops/"reponame".git`

## Gitignore
### what  to ignore
- Ignore things that can be generated (e.g. compiled code, minified files, etc.)
- Ignore dependencies (e.g. node_modules, venv, packages, etc.)
- Ignore things that are personal or specific to how you like to work (e.g. editor settings)
- Ignore things that are sensitive or dangerous (e.g. .env files, passwords, API keys, etc.)

### Pattern
- \* matches any number of characters except for a slash (/).
- / anchored to the directory containing the .gitignore. For example, this would ignore a main.py in the root directory, but not in any subdirectories.
- ! negate a pattern. For example, to ignore all .txt files except for important.txt *.txt !important.txt
- \# comments

## Weird case
```bash
# rename author and email probably because private email protection
git commit --amend --reset-author --no-edit # for last commit

# rename author and email ammend all commit after commit hash
git rebase -i "COMMITHASH" -x "git commit --amend --author 'francistops <65456051+francistops@users.noreply.github.com>' -CHEAD"
```


