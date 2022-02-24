def main():
    print("Hello git")



def git_steps():
    print("Follow the steps for pushing a project to github.")
    print("1.Create a repo")
    print("2.git init -> initialize an empty repository including your local files ")
    print("3. git add . -> adds all the files in the current folder queue, not yet committed")
    print("4. git status -> view all the files which are going to be staged in the first commit")
    print("5. git commit -m ''your message'' -> adds the changes to the local repository ")
    print("6. git remote add origin 'repo url'sini ekle' -> adds the repo where the code will be pushed")
    print("7. git push -u origin master ->, sometimes a force push is needed (-f)! push the code to your local repository")
    print()
    print("************** UPDATING THE PROJECT ************")
    print()
    print(" cd into your project through terminal ")
    print(" 1. git add . -> adds your modified files to the queue to be committed later. Files are not committed")
    print(" 2. git status -> view the changed files")
    print(" 3. git commit -m ''write here the revisions made in your code briefly'' ->commits the files that have been added and ")
    print(" creates a new revision with a log... ")
    print(" 4. git push -u origin master -> pushes your changes to the remote repository.   NOTE: sometimes you need a force push although not recommended")
    print()
    print("*********** Reminders **************")
    print("git push origin HEAD:master -> HEAD points to the top of the current branch. git can obtain the branch name from that.")
    print("My branch was not right -> git branch -> git branch -M master -> makes the main branch master")
    

if __name__ == "__main__":
    main()
    git_steps()