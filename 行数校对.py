import os

path=os.getcwd()
path2=path+"/一次机翻_对照组/"
path3=path+"/nene/"

for file in os.listdir(path3):
    if file.split(".")[-1]=="txt":
        f1=open(path3+file,'r')
        f2=open(path2+file,'r')
        num1=len(f1.readlines())
        num2=len(f2.readlines())
        print(file)
        if num1!=num2:
            print(file,error)
        f1.close()
        f2.close()
        

        
