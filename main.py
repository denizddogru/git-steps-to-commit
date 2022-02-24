def main():
    print("Hello git")



def git_steps():
    print("Follow the steps for pushing a project to github.")
    print("1.Create a repo")
    print("2.git init -> initialize an empty repository including your local files ")
    print("3. git add . -> adds all the files in the current folder")
    print("4. git status -> view all the files which are going to be staged in the first commit")
    print("5. git commit -m 'your message' -> adds the changes to the local repository ")
    print("6. git remote add origin 'repo url'sini ekle' -> adds the repo where the code will be pushed")
    print("7. git push -u origin master ->, sometimes a force push is needed (-f)! push the code to your local repository")
    print()
    print("*********** PULL REQUESTS **************")
    print("")

if __name__ == "__main__":
    main()
    git_steps()