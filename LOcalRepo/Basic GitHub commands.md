GITHUB COMMANDS

What is Git? Git is a version control system(which is a tool that helps to track changes in code) also used for collaboration. It is:- popular, free and open source and scalable as well.

What is Github? It is basically a website that allows developers to store as well as manage their code using Git.

Git Bash Git Bash is a command-line interface for Windows that provides a Unix-like environment, allowing users to run Git commands and other shell utilities seamlessly. It’s part of the Git for Windows package and includes a minimal Bash shell.

Configuring a Git Configuring Git means setting up user preferences and options to ensure Git works efficiently for your projects. SYNTAX:- git config --global user.name "My Name" git config --global user.email "email"

Basic Commands i. Clone command:-It basically clones a repository on our local machine. Syntax:- git clone <-some link->

ii. Status command:- It displays the current status of the code. Syntax:-git status There are four kinds of status used in Github

untracked- There are some new files that git doesn't track as of now.
modified- If we have made changes to the file.
staged-If we add something to the file then that process is staged.(after adding we commit that means finally our file will be unchanged)
unmodified-If we have made no changes to the file.

iii. cd command:-It stands for change directory. If we want to go out for outside folder to inside folder we can use this command.

iv. Add command:-It adds new or changed files in our current directory to the Git staging area. Syntax:-git add<-file name->

v. Commit command:- It basically gives the record of the changes that are done. Syntax:- git commit -m "some message"

vi. Push command:-We basically use this command to push our local system into Github.(local to remote) Syntax:- git push origin main(branch)/git push -u origin main where -u stands for setting upstream. Upstream means that if we want to work on a project for a long time we don't want to write origin main again and again and thus we use -u and where origin means the default repository

vii. Init command:-Used to create a new Git repository. Syntax:- git init For adding new repo:- git remote add origin<-link-> For checking branch:- git branch(project/product different copies are referred to as branch) For renaming branch:- git branch -M main

WORKFLOW First we create Github repo ---clone--changes--add--commit

BRANCH COMMANDS git branch-to check branch git branch -M main -to rename our branch git checkout <-branch name->-If we want to jump from one branch to another we use this command. git checkout -b <-new branch name->-If we want to create a new branch. git checkout -d<-branch name->-If we want to delete a branch.

MERGING CODE If we want to merge main with the other branches we can do the following:

git diff<-branch name-> (to compare commits, branches, files and more) git merge<-branch name-> (to merge 2 branches)
 2.Using Github We create a PR(pull request) 
             Pull request:-It basically lets you tell others about changes we have pushed to a           branch in a GitHub repository. 
viii. Pull command:-It lets you take and download content from a remote repository and immediately update the local repository to match that content. Syntax:- git pull origin main

UNDOING CHANGES Case1:staged changes(Basically those changes that are added but not committed yet) git reset<-file name-> git reset Case2:committed changes(for one commit)() git reset HEAD-1 Case3:committed changes(for many commits) git reset<-commit hash-> git reset --hard<-commit hash->

FORK:-It is basically a new repo that shares code  and visibility settings with other repos. It is basically a rough copy.
