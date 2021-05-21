import os

path=os.getcwd()
path2=path+"/Text/nene映射/"
num=0
for file in os.listdir(path2):
    if file.split(".")[-1]=="txt":
        f=open(path2+file,'r')
        zf=open(path+"/Text/nene_映射标号/"+file,"w+")
        line=f.readline()
        while line:
            line=line.replace("\n","")
            line=line+" __"+file.split(".")[0]+"_"+str(num)+"\n"
            zf.write(line)
            line=f.readline()
            num=num+1
        f.close()
        zf.close()
        num=0
        
