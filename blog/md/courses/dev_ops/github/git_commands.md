# Git Commands

This document collects some commands for you to learn more about git.

For the first time, you could git clone repos, your own repo or others repo without any problem, but if you ever want to commit and push code back 
to the remote, you would need to configure your password.

### **SETUP & CONFIG**

Configuring user information used across all local repositories. I would highly recommend everyone do the following to save troubles for the future.

`git config --global user.name “[firstname lastname]”`

set a name that is identifiable for credit when review version history.

`git config --global user.email “[valid-email]”`

set an email address that will be associated with each history marker.

`git config --global color.ui auto`

set automatic command line coloring for Git for easy reviewing.

`git config --global core.editor "vim"`

set `vim` to be your default editor in command line.

### INIT

Configuring user information, initializing and cloning repositories

*`git init`*

initialize an existing directory as a Git repository. 

> Try to get a new directory and do `git init` and then do a `ls -al` and see what changes you can find out.

### GIT CLONE

There are many usages of clone, most likely you would just need the simplest but just in case you would need more complex cases, you
can learn these examples.

`git clone [url]`

retrieve an entire repository from a hosted location via URL

`git clone --depth <number> [url]`

Limits the history to a specified number of commits.

**Example:**

`git clone --depth 5 [url]`

This command will clone the repository with the latest 5 commits.

`git clone --shallow-since=<date> [url]`

allows you to clone the repository with commits after a specific date

**Example:**

`git clone --shallow-since=2021-01-01 [url]`

This command will clone the repository with commits made after January 1, 2021.

`git clone --shallow-exclude=<revision> [url]`

excludes commits reachable from a specified revision.

**Example:**

`git clone --shallow-exclude=<commit-hash> [url]`

This command will clone the repository and exclude commits reachable from the specified commit hash.

`git clone --branch <branch-name> --single-branch --depth <number> [url]`

allows you to clone a specific branch with a limited history

**Example:**

`git clone --branch feature-branch --single-branch --depth 3 [url]`

This command will clone only the feature-branch with the latest 3 commits.

### **STAGE & SNAPSHOT**

Working with snapshots and the Git staging area. These are the most important commands you would need.

**status**

The `status` check what files have been tracked or not tracked by git.

`git status`

show modified files in working directory, staged for your next commit

**add**

`git add [file]`

add a file as it looks now to your next commit (stage)

**reset**

If there is a file, that becomes green, and you regret it and you want to put it back, meaning making it look red again, then you use this command.

`git reset [file]`

unstage a file while retaining the changes in working directory

**diff**

use `diff` to check what changes you made in each file.

`git diff`

diff of what is changed but not staged

`git diff --staged`

**commit**

This command will create a batch job, bundle all the files to be pushed and created a hash.

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

## Ref

* <https://education.github.com/git-cheat-sheet-education.pdf>
