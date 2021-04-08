1)      What is GIT?
ans.    Git is a software .It is used for tracking changes in any set of files, usually used for 
        coordinating work among programmers collaboratively developing source code during software development 

2)      What is a repository in GIT?
ans     A GIT repository allows performing various operations on it to create different versions of a project.

3)      What is the command you can use to write a commit message?
ans      git commit is to use the command git commit -m "Git commit message here" .

4)      What is the difference between GIT and SVN?
ans      Git is a distributed version control system, whereas SVN is a centralized version control system.

5)      What are the advantages of using GIT?
ans     One of the biggest advantages of Git is its branching capabilities. Unlike centralized version control systems,
        Git branches are cheap and easy to merge. This facilitates the feature branch workflow popular with many Git users.

6)      What language is used in GIT?
ans     Python ,c++,c,perl,etc.

7)      What is the function of ‘GIT PUSH’ in GIT?
ans     The git push command is used to upload local repository content to a remote repository.

8)      Why GIT better than Subversion?
ans     It is powerful and cheap branching with easy merge in which each developer has his repository and 
        have a local copy in which they can change .

9)      What is “Staging Area” or “Index” in GIT?
ans     The Git index is used as a staging area between your working directory and your repository.

10)   What is GIT stash?
ans   The git stash command takes your uncommitted changes (both staged and unstaged), saves them 
      away for later use, and then reverts them from your working copy.

11)   What is GIT stash drop?
ans   Git stash is a temporary storage. When you're ready to continue where you left off, you can 
      restore the saved state easily.

12)   How will you know in GIT if a branch has been already merged into master?
ans   Run command git merge-base <commit-hash-step1> <commit-hash-step2> . If output of step 3 is
     same as output of step 2, then a "branch" has been already merged into master.

13)   What is the function of git clone?
ans   git clone is primarily used to point to an existing repo and make a clone or copy 
     of that repo at in a new directory, at another location.

14)   What is the function of ‘git config’?
ans   The git config command is a convenience function that is used to set Git configuration 
      values on a global or local project level.

15)   What does commit object contain?
ans   The commit object contains the directory tree object hash, parent commit hash, 
     author, committer, date and message.

16)   How can you create a repository in Git?
ans   1.Create a directory to contain the project.
       2.Go into the new directory.
        3.Type git init .
         4.Write some code.
          5.Type git add to add the files (see the typical use page).
           6.Type git commit .

17)   What is ‘head’ in git and how many heads can be created in a repository?
ans   A repository can contain any number of heads. When you checkout to any branch the HEAD
      revision changes to the latest commit of the new branch. We directly will not create head but when we commit,
      git creates a reference to that commit known as head.

18)   What is the purpose of branching in GIT?
ans   In Git, branches are a part of your everyday development process. Git branches are effectively a 
      pointer to a snapshot of your changes.

19)   What is the common branching pattern in GIT?
ans   It's common to create, work on, merge, and delete branches several times a day.

20)   How can you bring a new feature in the main branch?
ans    After creating a branch, check it out locally so that any changes you make will be on that branch.
       This checks out a branch called new-feature based on master , and the -b flag tells Git to create 
        the branch if it doesn't already exist.

21)   What is a ‘conflict’ in git?
ans    A conflict arises when two separate branches have made edits to the same line in a file, 
      or when a file has been deleted in one branch but edited in the other. Conflicts will most 
      likely happen when working in a team environment.


22)   How can conflict in git resolved?
ans   1.The easiest way to resolve a conflicted file is to open it and make any necessary changes.
       2.After editing the file, we can use the git add a command to stage the new merged content.
         3.The final step is to create a new commit with the help of the git commit command.
          4.Git will create a new merge commit to finalize the merge.

23)   To delete a branch what is the command that is used?
ans    The -d option will delete the branch only if it has already been pushed and merged with the remote branch.
       Use -D instead if you want to force the branch to be deleted, even if it hasn't been pushed or merged yet.

24)   What is another option for merging in git?
ans   Using git rebase Instead of git merge.

25)   What is GIT version control?
ans   Version control is a system that records changes to a file or set of files over time so that you can
      recall specific versions later.

26)    What is the function of ‘git diff ’ in git?
ans    git diff is a multi-use Git command that when executed runs a diff function on Git data sources.

27)     What is ‘git status’ is used for?
ans    The git status command displays the state of the working directory and the staging area.

28)   What is the difference between the ‘git diff ’and ‘git status’?
ans   If you need some of your files, not to be tracked or listed inside the git status command(which 
      means you don't want some files to be present in any of your commits) then you can include patterns 
      of those files in. “git diff --cached.

29)   What is the function of ‘git checkout’ in git?
ans   The git checkout command lets you navigate between the branches created by git branch.

30)   What is the function of ‘git rm’?
ans   The git rm command can be used to remove individual files or a collection of files.

31)   What is the function of ‘git stash apply’?
ans   git stash temporarily shelves (or stashes) changes you've made to your working copy so
      you can work on something else, and then come back and re-apply them later on.

32)   What is the use of ‘git log’?
ans   Git log command is used when you want to check Git add, Git add all and Git commit history 
      made by you or other user.

33)   What is ‘git add’ is used for?
ans   Git add  adds all modified and new (untracked) files in the current directory .

34)   What is the function of ‘git reset’?
ans   Git reset is a powerful command that is used to undo local changes to the state of a Git repo.

35)   Explain what is commit message?
ans   The commit command is used to save changes to a local repository after staging in Git. However, 
      before you can save changes in Git, you have to tell Git which changes you want to save as you might have made tons of edits.

36)   Name a few Git repository hosting services
ans   1: GitHub. Seriously, this is a valid option.
       2: GitLab. GitLab is probably the leading contender when it comes to alternative code platforms.
         3: Bitbucket. Bitbucket has been around for many years. 
          4: SourceForge. 
            5: Roll your own. 
             6: All of the above.
