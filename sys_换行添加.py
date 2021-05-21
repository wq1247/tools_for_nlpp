import os
import time,re
path=os.getcwd()
ch1=open(path+"/sys_jpn.txt",'r')
f=open(path+"/修正sys_text.txt",'r')
o=open(path+"/修正sys_text2换行.txt",'w+')
j_lines = ch1.readlines()
c_lines = f.readlines()
n=0
for j_line in j_lines:
    c_line=c_lines[n]
    c_line=c_line.replace("◙","")
    i=j_line.count("◙")
    #print(i)
    if i!=0:
        i=j_line.index("◙")
        l=len(c_line)
        try:
            while i:
                #print(i,c_line)
                if i >= l:
                    break
                c_line=c_line[0:i]+"◙"+c_line[i:]
                i=j_line.index("◙",i+1)
        except:
            i=0
    c_lines[n]=c_line
    n=n+1
for line in c_lines:
    o.write(line)
o.close()
print("完成")
