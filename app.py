import os

## Number of days you want to make commits
for i in range(20):
    d = str(i) + ' check the code tasks to be done:'
    ## Open a text file and modify it
    with open('CodeTasksToDo.py', 'a') as file:
        file.write(d+'\n')
    ## Add bot.txt to staging area
    os.system('git add CodeTasksToDo.py')
    ## Commit it
    os.system('git commit --date="' + d + '" -m "Exercise commit"')

## push the commit to github
os.system('git push -u origin master')