import os

txt=open("sys_text2_换行映射.txt","r")
orl=open("orlookup.txt",'r')
out=open("sys映射完_out.txt","w+")
lookup=orl.readlines()
lo=[]
for l in lookup:
    lo.append(l[0])
c_data=[]
txt=txt.readlines()
for line in txt:
    for c in line:
        try:
            i=c_data.index(c)
        except:
            c_data.append(c)
for c in c_data:
    if lo.count(c)==0:
        out.write(c)
out.close()

    
    
