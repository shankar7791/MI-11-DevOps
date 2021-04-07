1)      What is GIT?
Ans: Git is a version control system for tracking changes in computer files and coordinating work on            those files among multiple people


2)      What is a repository in GIT?
Ans : repository is a directory or storage space where your projects can live. It can be local to a folder             on your computer, or it can be a storage space on GitHub or another online host. We can keep 	           code files, text files, image files, we name it, inside a repository.


3)      What is the command you can use to write a commit message?
ANS: command to write a commit message :- git commit -m "Git commit message here".


4)      What is the difference between GIT and SVN?
Ans : The difference between Git and SVN version control systems is that Git is a distributed version            control system, whereas SVN is a centralized version control system. 


5)      What are the advantages of using GIT?
Ans: One of the biggest advantages of Git is its branching capabilities. Unlike centralized version           control systems, Git branches are cheap and easy to merge.


6)      What language is used in GIT?
Ans: Mostly "c" language used in Git.

7)      What is the function of ‘GIT PUSH’ in GIT?
Ans : The git push command is used to upload local repository content to a remote repository.

8)      Why GIT better than Subversion?
Ans :Git better than subversion because  it's faster to commit.We commit to the central repository more often in SVN, network traffic slows everyone down. Whereas with Git, you're working mostly on your local repository and only committing to the central repository every so often.

9)      What is “Staging Area” or “Index” in GIT?
Ans :The staging area is like a rough draft space, it's where we  can git add the version of a file or multiple files that we want to save in our next commit.

10)   What is GIT stash?
Ans :The git stash command takes your uncommitted changes (both staged and unstaged), saves them away for later use, and then reverts them from your             working copy.

11)   What is GIT stash drop?
Ans :In case we do not need a specific stash, we use git stash drop command to remove it from the list of stashes.

12)   How will you know in GIT if a branch has been already merged into master?
Ans :We  can use the git merge-base command to find the latest common commit between the two branches. If that commit is the same as our branch head, then              the branch has been completely merged.

13)   What is the function of git clone?
Ans :Git clone is primarily used to point to an existing repo and make a clone or copy of that repo at in a new directory, at another location.

14)   What is the function of ‘git config’?
Ans :The git config command is a convenience function that is used to set Git configuration values on a global or local project level.

15)   What does commit object contain?
Ans :The commit object contains the directory tree object hash, parent commit hash, author, committer, date and message.

16)   How can you create a repository in Git?
Ans :Start a new git repository
            1. Create a directory to contain the project.
            2. Go into the new directory.
            3.Type git init .
           4.Write some code.
           5.Type git add to add the files (see the typical use page).
           6.Type git commit .

17)   What is ‘head’ in git and how many heads can be created in a repository?
Ans :The 'head' points out the last commit in the current checkout branch. It is like a pointer to any reference.A repository can contain any number of 'heads'.

18)   What is the purpose of branching in GIT?
Ans : Branching is used to maintain stability while isolated changes are made to code. Branching facilitates the development of bug fixes, the addition of new              capabilities and the integration of new versions after they have been tested in isolation.

19)   What is the common branching pattern in GIT?
Ans :Git-Flow

20)   How can you bring a new feature in the main branch?
Ans :First, we need to make sure our local master is synchronized with the upstream master . Then, we merge the feature branch into master and push the                          updated master back to the central repository. 

21)   What is a ‘conflict’ in git?
Ans :  A conflict in git arises when two separate branches have made edits to the same line in a file, or when a file has been deleted in one branch but edited in                     the  other.

22)   How can conflict in git resolved?
Ans :Ways to solve Git conflict:
             1.The easiest way to resolve a conflicted file is to open it and make any necessary changes.
            2.After editing the file, we can use the git add a command to stage the new merged content.
            3.The final step is to create a new commit with the help of the git commit command.
           4.Git will create a new merge commit to finalize the merge. 

23)   To delete a branch what is the command that is used?
Ans :'git branch -D  'my-branch'.

24)   What is another option for merging in git?
Ans : Using git rebase .

25)   What is GIT version control?
Ans : Version control, also known as source control, is the practice of tracking and managing changes to software code. Version control systems are software tools               that help software teams manage changes to source code over time.

26)    What is the function of ‘git diff ’ in git?
Ans : Diff command is used in git to track the difference between the changes made on a file. Since Git is a version control system, tracking changes are              something very vital to it. Diff command takes two inputs and reflects the differences between them.

27)     What is ‘git status’ is used for?
Ans : The git status command displays the state of the working directory and the staging area. It lets you see which changes have been staged, which haven't,                     and which files aren't being tracked by Git.

28)   What is the difference between the ‘git diff ’and ‘git status’?
Ans : git diff is a multi-use Git command that when executed runs a diff function on Git data sources and git status command displays the state of the working directory and the staging area. 

29) What is the function of ‘git checkout’ in git?
Ans : The 'git checkout' command lets you navigate between the branches created by git branch . Checking out a branch updates the files in the working                            directory to match the version stored in that branch, and it tells Git to record all new commits on that branch.

30) What is the function of ‘git rm’?
Ans : The primary function of git rm is to remove tracked files from the Git index.

31)   What is the function of ‘git stash apply’?
Ans : Apply the changes without removing stored files from stash area.

32)   What is the use of ‘git log’?
Ans :'Git log' is a utility tool to review and read a history of everything that happens to a repository.

33)   What is ‘git add’ is used for?
Ans :It adds all modified and new (untracked) files in the current directory and all subdirectories to the staging area (a.k.a. the index), thus preparing them to be             included in the next git commit .

34) What is the function of ‘git reset’?
Ans : 'Git reset' is a command that is used to undo local changes to the state of a Git repo.

35)   Explain what is commit message?
Ans :The commit command is used to save changes to a local repository after staging in Git. However, before  we save changes in Git, we have to tell Git                                 which changes we want to save as we might have made tons of edits. A great way to do that is by adding a commit message to identify our changes.

36)   Name a few Git repository hosting services
Ans : Amazon AWS CodeCommit, Bitbucket, GitLab, Microsoft Azure,Perforce.
