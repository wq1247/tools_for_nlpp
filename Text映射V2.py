import os
import time,re
path=os.getcwd()
ch1=open("char映射.txt",'r')
char1=ch1.readlines()
f=open(path+"/sys_text2.txt",'r')
o=open(path+"/sys_text2_映射.txt",'w+')
line = f.readline()
charor=[]
for cha in char1:
    charor.append(cha[1])
while line:
    tr=False
    data=""
    #line=line.replace('姉','姐').replace('嶺','岭').replace("愛","爱").replace("●","我")
    #line=line.replace("●","我")
    line=line.replace("\n","")
    for num in range(len(line)):
        if line[num]=='▲':
            tr=bool(1-tr)
#               print(line[num],tr)
        if tr:
            data=data+line[num]
        else:
            try:
                i=charor.index(line[num])
                data=data+char1[i][0]
#                print(data)
            except:
                data=data+line[num]
    line=data+"\n"
    o.write(line)
    line=f.readline()
f.close()
o.close()
print("完成")
