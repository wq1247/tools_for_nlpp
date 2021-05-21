import os

txt=open("sys_字频.txt","r")
ej=open("EJchar.txt","r")
#orl=open("orlookup.txt",'r')
out=open("sys_字频2.txt","w+")
#lookup=orl.readlines()
ej_c=[]
ej=ej.readline()
for c in ej:
    ej_c.append(c)
num=0
txt=txt.readlines()
for line in txt:
    c=line[0]
    i=ej_c.count(c)
    if i!=0:
        txt.pop(num)
    num=num+1
for i in txt:
    out.write(i)
out.close()

    
    
