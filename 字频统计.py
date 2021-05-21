import os

txt=open("sys_text2.txt","r")
#orl=open("orlookup.txt",'r')
out=open("sys_字频.txt","w+")
#lookup=orl.readlines()
c_num=[]
c_data=[]
txt=txt.readlines()
for line in txt:
    for c in line:
        try:
            i=c_data.index(c)
            c_num[i]=c_num[i]+1
        except:
            c_data.append(c)
            c_num.append(1)
for i in range(len(c_data)):
    out.write(c_data[i]+"   "+str(c_num[i])+"\n")
out.close()

    
    
