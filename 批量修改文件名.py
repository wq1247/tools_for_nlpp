import os

root0=os.getcwd()
for root, dirs, files in os.walk(root0):
#root当前路径 dirs当前路径下文件夹组 files当前路径下文件名称
#若dirs为空则证明当前路径为最小路径
    if dirs==[]:
        print(root)
        for file in files:
            if file.split(".")[0]!='':
                name=file.split(".")[1]+".bclim.00.png"
                name=name.split("-")[1]
                print(file,name)
                os.rename(root+"/"+file,root+"/"+name)
