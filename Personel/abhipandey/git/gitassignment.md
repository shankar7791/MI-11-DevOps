1 : git is a mature actively maintained open source project originally    developed by linus torvalds in 2005.

2 : A git repository .git/ folder inside a project,it tracks all th    changes made in the project.

3 : git commit -m "message"

4 : the difference between git and SVN version control system is that
    git is a distributed control system , whereas SVN is a centralized    control system.

5 : one of the biggest advantage of using git is its branching abilit    -es . Git branches are cheap and easy to merge. 
    feature branches provide isolated environment for every change to     code base.

6 : languages used in git are python , C , C++ , Perl.

7 : The function of git push is used to upload local repository conten    to a remote repository.Pushing is how transfer ccommits fro    local repository to remote repository.

8 : git has the advantage that its much better suited if some 
    developers are not connected to master repository.It is much faste    than SVN.

9 : Staging area is a rough draft space where we can git add the 
    version of a file or file that wants to save in next commit.

10 : git stash temporarily shelves changes made to the working copy
     so we can work on something else and then comeback and reapply 
     later on.

11 : dropping a stash will change the stash designation of all the 
     stashes further down the stack .

12 : step 1 - switch to master branch " git checkout master "
     step 2 - take all the commits from the bugfix branch an merge it
              with current branch "git merge --squash bugfix "
     step 3 - create single commit from merged changes 
              " git commit "

13 : git clone command copies an existing git repository

14 : the git config command is convinence function that is used to set     git configuraton values on global or local project level.

15 : the commit object contains the directory tree object hash , commi     -tter,date and message.

16 : a -create a directory to contain the project
     b -go into the new directory
     c -type git init
     d -write some code
     e -write git add to add the files
     f - type git commit

17 : head is simply a reference to the last commit in the current worki     ng branch . There will be a default head known as master.A 
     repository can contain n number of heads.

18 : Git branches are efffectively a pointer to a snapshot of your c     changes.

     Branches is used in version control and software management to 
     maintain stability while changes are made to code

19 : Release > Production deployment master > most stable tested brn     branch deployed on staging all other branches > one braanch for
     each feature.

20 : 1- start with master branch 
     2- create a new branch
     3- update , add , commit and push changes
     4- push feature branch to remote
     5- merge your pull request

21 : A conflict arises when two seperate branches have made edits to 
     the same line in a file or file has been deleted in a branch bu      but edited in other.

22 : 1- Under the repository name click pull request 
     2- in the pull request select the pull request with merge conflic        that needs to be resolved
     3- near the bottom of pull request click resolve conflicts.
     4- decide if you want to keep only your branch changes .
     5- once you resolved the conflict mark as resolved.

23 : git branch -D my-branch is the command.

24 : the another opton of merging in git is rebase 
     
25 : Version control system is a system that records chaanges to the f     file or set of file so that we can call specific version later.

26 : diffing is a function that takes two input data sets and output 
     the changes between them.
     git diff is a multi use git commands that when executed runs diff     function on git data sources.

27 : the git status command displays the state of the working director     and the staging area.

28 : git diff returns the name of the file who are ready to be staged
     on the next commit.
     git status provide the details of the file and also the compariso     with the origin of branch.

29 : git checkout command lets you navigate between the branches creat     by git branch

30 : The git rm command can be used to remove file or a collection of      files.

31 : git stash apply applies the changes without removing stored files     from stash area.

32 : git log is a repository tool to review and read a history of 
     everything that happens to a repository.

33 : git add command adds a change in the working directory to the sta     staging area.

34 : git reset is a powerfull command that is used to undo local chang     changes to the state of a git repo.

35 : The commit command is used to change to a local repositoryafter s    staging in git.

36 : Few git hosting repository are 
    1 GitLab
    2 BitBucket
    3 SourceForge
    4 LaunchPad
    5 Gogs
