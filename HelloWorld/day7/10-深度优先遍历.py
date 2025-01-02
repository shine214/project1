import os

#1
def dfs(path):
    for i in os.listdir(path):
        full_path = os.path.join(path, i)
        if(os.path.isdir(full_path)):
            dfs(full_path)
        else:
            print(full_path)
dfs(os.getcwd())