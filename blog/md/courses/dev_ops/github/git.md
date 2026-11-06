# Git Ref

## Cheatsheet

### **SETUP**

Configuring user information used across all local repositories

`git config --global user.name “[firstname lastname]”`

set a name that is identifiable for credit when review version history

`git config --global user.email “[valid-email]”`

set an email address that will be associated with each history marker

`git config --global color.ui auto`

set automatic command line coloring for Git for easy reviewing


### **SETUP & INIT**

Configuring user information, initializing and cloning repositories

`git init`

initialize an existing directory as a Git repository

`git clone [url]`

retrieve an entire repository from a hosted location via URL

`git clone --depth <number> [url]`


Limits the history to a specified number of commits.

Example:

`git clone --depth 5 [url]`

This command will clone the repository with the latest 5 commits.

`git clone --shallow-since=<date> [url]`

allows you to clone the repository with commits after a specific date

Example:

`git clone --shallow-since=2021-01-01 [url]`

This command will clone the repository with commits made after January 1, 2021.

`git clone --shallow-exclude=<revision> [url]`

excludes commits reachable from a specified revision.

Example:

`git clone --shallow-exclude=<commit-hash> [url]`

This command will clone the repository and exclude commits reachable from the specified commit hash.

`git clone --branch <branch-name> --single-branch --depth <number> [url]`

allows you to clone a specific branch with a limited history

Example:

`git clone --branch feature-branch --single-branch --depth 3 [url]`

This command will clone only the feature-branch with the latest 3 commits.

### **STAGE & SNAPSHOT**

Working with snapshots and the Git staging area

`git status`

show modified files in working directory, staged for your next commit

`git add [file]`

add a file as it looks now to your next commit (stage)

`git reset [file]`

unstage a file while retaining the changes in working directory

`git diff`

diff of what is changed but not staged

`git diff --staged`

diff of what is staged but not yet commited

`git commit -m “[descriptive message]”`

commit your staged content as a new commit snapshot


### **BRANCH & MERGE**

Isolating work in branches, changing context, and integrating changes

`git branch`

list your branches. a * will appear next to the currently active branch

`git branch [branch-name]`

create a new branch at the current commit

`git checkout`

switch to another branch and check it out into your working directory

`git merge [branch]`

merge the specified branch’s history into the current one

`git log`

show all commits in the current branch’s history

### **TEMPORARY COMMITS**

Temporarily store modified, tracked files in order to change branches

`git stash`

Save modified and staged changes

`git stash list`

list stack-order of stashed file changes

`git stash pop`

write working from top of stash stack

`git stash drop`

discard the changes from top of stash stack

**SHARE & UPDATE**

Retrieving updates from another repository and updating local repos

`git remote add [alias] [url]`

add a git URL as an alias

`git fetch [alias]`

fetch down all the branches from that Git remote

`git merge [alias]/[branch]`

merge a remote branch into your current branch to bring it up to date

`git push [alias] [branch]`

Transmit local branch commits to the remote repository branch

`git pull`

fetch and merge any commits from the tracking rem

### **TRACKING PATH CHANGES**

Versioning file removes and path changes

`git rm [file]`

delete the file from project and stage the removal for commit

`git mv [existing-path] [new-path]`

change an existing file path and stage the move

`git log --stat -M`

show all commit logs with indication of any paths that moved

### **INSPECT & COMPARE**

Examining logs, diffs and object information

`git log`

show the commit history for the currently active branch

`git log branchB..branchA`

show the commits on branchA that are not on branchB

`git log --follow [file]`

show the commits that changed file, even across renames

`git diff branchB...branchA`

show the diff of what is in branchA that is not in branchB

`git show [SHA]`

show any object in Git in human-readable format

### **IGNORING PATTERNS**

Preventing unintentional staging or commiting of files

```
logs/
*.notes
pattern*/
```

matches or wildcard globs.

Save a file with desired paterns as .gitignore with either direct string 

`git config --global core.excludesfile [file]`

system wide ignore patern for all local repositories

### **REWRITE HISTORY** 

**Rewriting branches, updating commits and clearing history**

`git rebase [branch]`

Reapply the commits from the current branch onto the specified branch, effectively changing the base of the current branch to the specified branch.

**Example 1: Basic Rebase**

Let's assume we have the following commit history:

main: A---B---C
             \
              D---E---F feature

We want to rebase the feature branch onto main to incorporate the latest changes from main:

`git checkout feature`

`git rebase main`

After rebasing, the commit history will look like:

main: A---B---C
                 \
                  D'---E'---F' feature


`git rebase -i [commit]`

Interactively rebase the current branch onto [commit].The -i flag stands for "interactive." It allows you to interactively rebase your commits, which means you can choose to edit, reorder, squash, or drop commits.

**Example 2: Interactive Rebase (git rebase -i)**

Suppose we have the following commit history on a branch:

feature: A---B---C---D---E

We want to squash the commits C and D together and reword the commit message of E:

`git checkout feature`

`git rebase -i HEAD~3`

This will open an editor with the last three commits:

pick C Commit message for C

pick D Commit message for D

pick E Commit message for E

We can modify it to:

pick C Commit message for C

squash D Commit message for D

reword E Commit message for E

After saving and closing the editor, Git will prompt you to modify the commit messages. After making the necessary changes, the commit history will look like:

feature: A---B---C'---E'

`git rebase --continue`

Continue the rebase process after resolving conflicts.

**Example 3: Continue a Rebase**

`git rebase main`

`git add <resolved-files>`

`git rebase --continue`

`git rebase --abort`

Abort the rebase and return to the original state

**Example 4: Abort a Rebase**

`git rebase main`

`git rebase --abort`

`git rebase --skip`

Skip the commit that caused conflicts.

**Example 4: Skip a Commit**

`git rebase main`

`git rebase --skip`

`git rebase -onto [newbase] [upstream] [branch]`

Rebase selected commits onto another base.

**Example 5: Rebase with a Conflict Resolution**

Imagine you have the following history:

main: A---B
             \
              C---D feature

You start a rebase and encounter a conflict:

`git checkout feature`

`git rebase main`

### **Resolve conflicts in the files**

`git add <resolved-files>`

`git rebase --continue`

`git reset --hard [commit]`

clear staging area, rewrite working tree from specified commit

`git revert [commit]`

Create a new commit that undoes the changes made in the specified commit.

`git reset --soft [commit]`

Move the HEAD pointer to [commit], staging all changes.

`git reset --hard [commit]`

Move the HEAD pointer to [commit], discarding all changes in the working directory.

`git commit --amend -m "[new message]"`

Change the commit message of the most recent commit.

### **Optimizing and managing commit history**

`git merge --ff-only [branch]`

Perform a fast-forward merge, failing if not possible.

`git merge --no-ff [branch]`

Perform a merge and always create a merge commit, even if a fast-forward is possible.

`git merge --squash [branch]`

Merge the changes from the specified branch, but do not create a merge commit. Instead, stage all the changes and prepare them to be committed in a single commit.

`git clone --depth 1 [url]`

Perform a shallow clone with a history truncated to the latest commit.


### **Authentication and configuration with tokens**

`git config --global credential.helper store`

Save your credentials to a file.

`git config --global user.name "your-username"`

Set your GitHub username.

`git remote set-url origin https://<token>@github.com/username/repo.git`

Set the remote URL with the access token for authentication.

## Github Access 

* Use token to access a project

If you want to join someone's project, that project owner has to add your github id as collaborator. Then in the project setting, the project owner will generate a token. For example, a `classic token` and send it to the collaborator. The collaborator will use the above way to set password. The id is your github username, and password is the token.

`git config --global credential.helper store`

Set your credentials to be stored.

`git remote set-url origin https://<token>@github.com/username/repo.git`

Use the token as the password when prompted.

* Use SSH

Generate a public key and save it to the github ssh to allow the server to know your machine information. 

`ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`

Generate a new SSH key.

`ssh-add ~/.ssh/id_rsa`

Add your SSH key to the SSH agent.

`cat ~/.ssh/id_rsa.pub`

Copy your SSH public key and add it to your GitHub account.

## Trigger github.io to rebuild

`git commit -m 'rebuild pages' --allow-empty`
`git push origin <branch_name>`

## A new set of commands when you create a new repo in git

**Here is a complete example**

You have an empty repository
To get started you will need to run these commands in your terminal.

New to Git? Learn the basic Git commands

**Configure Git for the first time**

```shell
git config --global user.name "Kevin Li"
git config --global user.email "id@email.com"
```

**Working with your repository**

I just want to clone this repository
If you want to simply clone this empty repository then run this command in your terminal.

`git clone https://coderepo.mobilehealth.va.gov/scm/vamfdtr/mlops-test.git`

**My code is ready to be pushed**

If you already have code ready to be pushed to this repository then run this in your terminal.

```shell
cd existing-project
git init
git add --all
git commit -m "Initial Commit"
git remote add origin https://coderepo.mobilehealth.va.gov/scm/vamfdtr/mlops-test.git
git push -u origin HEAD:mlops-test
```

**My code is already tracked by Git**

If your code is already tracked by Git then set this repository as your "origin" to push to.

```shell
cd existing-project
git remote set-url origin https://coderepo.mobilehealth.va.gov/scm/vamfdtr/mlops-test.git
git push -u origin --all
git push origin --tags
```

## Ref

* <https://education.github.com/git-cheat-sheet-education.pdf>
