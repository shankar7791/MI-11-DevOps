1)    Git is a version control system
       
2)   Git is a program that tracks changes made to files. ... A Git repository is the . git/ folder inside a project. This repository tracks all changes made to files in your project, building a history over time            

3)  git commit -m "uploading sdlc.md"

4)  The difference between Git and SVN version control systems is that Git is a distributed version     control system, whereas SVN is a centralized version control system. Git uses multiple repositories i ncluding a centralized repository and server, as well as some local repositories.

5)
    • Git has intigrity,
    •   snapshot capture in git
    • git genrally only add the data
    • .git folder save the snapshot
    • almost evry opration is local

6)    Python , c ,c++

7)   The git push command is used to upload local repository content to a remote repository. Pushing is how you transfer commits from your local repository to a remote repo. It's the counterpart to git fetch , but whereas fetching imports commits to local branches, pushing exports commits to remote branches.

8)   Git has the advantage that it's MUCH better suited if some developers are not always connected to the master repository. Also, it's much faster than SVN. And from what I hear, branching and merging support is a lot better (which is to be expected, as these are the core reasons it was written).
 
9)  The Git index is used as a staging area between your working directory and your repository. You can use the index to build up a set of changes that you want to commit together. When you create a commit, what is committed is what is currently in the index, not what is in your working directory.

10)  The git stash command takes your uncommitted changes (both staged and unstaged), saves them away for later use, and then reverts them from your working copy.

11)  Git stash is a temporary storage. When you're ready to continue where you left off, you can restore the saved state easily: git stash pop . Popping your stash removes the changes from your stash and reapplies the last saved state

12)  You can use the git merge-base command to find the latest common commit between the two branches. If that commit is the same as your branch head, then the branch has been completely merged.

13)  Usage. git clone is primarily used to point to an existing repo and make a clone or copy of that repo at in a new directory, at another location. The original repository can be located on the local filesystem or on remote machine accessible supported protocols. The git clone command copies an existing Git repository.
  
14)  The git config command is a convenience function that is used to set Git configuration values on a global or local project level. These configuration levels correspond to . gitconfig text files. Executing git config will modify a configuration text file.
  
15)   The commit object contains the directory tree object hash, parent commit hash, author, committer, date and message.

16)   Create a directory to contain the project.
Go into the new directory.
Type git init .
Write some code.
Type git add to add the files (see the typical use page).
Type git commit .

17)  A repository can contain any number of heads. When you checkout to any branch the HEAD revision changes to the latest commit of the new branch. We directly will not create head but when we commit, git creates a reference to that commit known as head.

18)  In Git, branches are a part of your everyday development process. Git branches are effectively a pointer to a snapshot of your changes. When you want to add a new feature or fix a bug—no matter how big or how small—you spawn a new branch to encapsulate your changes.

19)  But in Git it's common to create, work on, merge, and delete branches several times a day. You saw this in the last section with the iss53 and hotfix branches you created. You did a few commits on them and deleted them directly after merging them into your main branch.            

20)  First, you need to make sure your local master is synchronized with the upstream master . Then, you merge the feature branch into master and push the updated master back to the central repository. Pull requests can be facilitated by product repository management solutions like Bitbucket Cloud or Bitbucket Server.

21) Git can handle most merges on its own with automatic merging features. A conflict arises when two separate branches have made edits to the same line in a file, or when a file has been deleted in one branch but edited in the other. Conflicts will most likely happen when working in a team environment.

22)  How to Resolve Merge Conflicts in Git?
    • The easiest way to resolve a conflicted file is to open it and make any necessary changes.
    • After editing the file, we can use the git add a command to stage the new merged content.
    • The final step is to create a new commit with the help of the git commit command.
    • Git will create a new merge commit to finalize the merge.

23)  Delete a branch with git branch -d <branch> . The -d option will delete the branch only if it has already been pushed and merged with the remote branch. Use -D instead if you want to force the branch to be deleted, even if it hasn't been pushed or merged yet. The branch is now deleted locally.

24)  Using git rebase Instead of git merge. Using the "git merge" command is probably the easiest way to integrate changes from one branch into another. However, it's not your only option: "git rebase" offers another, slightly different way of integration.

25)  Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later. For the examples in this book, you will use software source code as the files being version controlled, though in reality you can do this with nearly any type of file on a computer.

26)   Diffing is a function that takes two input data sets and outputs the changes between them. git diff is a multi-use Git command that when executed runs a diff function on Git data sources. These data sources can be commits, branches, files and more

27)   The git status command displays the state of the working directory and the staging area. It lets you see which changes have been staged, which haven't, and which files aren't being tracked by Git. Status output does not show you any information regarding the committed project history.

28)   Whereas the git status command will display the whole current status of your working tree (files that are staged, modified, deleted, untracked etc.) ... For example, if you do git status -s , you will get all the differences from your working directory against your HEAD and your index including untracked files..

29)   The git checkout command lets you navigate between the branches created by git branch . Checking out a branch updates the files in the working directory to match the version stored in that branch, and it tells Git to record all new commits on that branch.

30)   The git rm command can be used to remove individual files or a collection of files. The primary function of git rm is to remove tracked files from the Git index. Additionally, git rm can be used to remove files from both the staging index and the working directory.

31)    git stash temporarily shelves (or stashes) changes you've made to your working copy so you can work on something else, and then come back and re-apply them later on

32)   Git log is a utility tool to review and read a history of everything that happens to a repository. Multiple options can be used with a git log to make history more specific. Generally, the git log is a record of commits.

33)  git add . adds all modified and new (untracked) files in the current directory and all subdirectories to the staging area (a.k.a. the index), thus preparing them to be included in the next git commit . Any files matching the patterns in the . gitignore file will be ignored by git add .

34)   To review, git reset is a powerful command that is used to undo local changes to the state of a Git repo. Git reset operates on "The Three Trees of Git". These trees are the Commit History ( HEAD ), the Staging Index, and the Working Directory.

35)   What is a commit message? The commit command is used to save changes to a local repository after staging in Git. However, before you can save changes in Git, you have to tell Git which changes you want to save as you might have made tons of edits.

36)
    •  GitHub
    • GitLab
    • Bitbucket SourceForge
    • Roll your own
    • All of the above
