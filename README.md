# AmazingAI
Project on a set of library methods of artificial intelligence.

Initiated by Articial Intelligence Lab, Telkom University, Indonesia.

# Contribution Flow
The first thing you should do is of course to create an account and [install git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) on your device.
After that, [clone](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) this project to the your own directory.

This repository development requires you to use [Branching WorkFlows](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows), in brief:

- Create your own branch from `master`, the branch describes what you want to develop, such as `updateRedme` or `initMainANN`, etc.
```
git checkout -b updateReadme
```
- Add your files that has been modified by you. 
```
git add .
```

or you can add a specific file
```
git add README.md
```

- Commit your changes on your branch.
```
git commit -m "gives your comment of your commit here"
```
- After all looks good, push your branch.
```
git push -u origin newFeatureBranch
```
- Create Pull Request from your branch to master.
- Wait reviewer to check your Pull Request and merge to the master.
