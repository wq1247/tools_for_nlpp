import os

txt=open("script字频2.txt","r")
sys=open("sys_字频2.txt","r")
#orl=open("orlookup.txt",'r')
out=open("总字频.txt","w+")
#lookup=orl.readlines()
txt=txt.readlines()
txt_num=[]
sys=sys.readlines()
txt_c=[]
for line in txt:
    txt_c.append(line[0])
    txt_num.append(line[2:-1])
for line in sys:
    c=line[0]
    n=line[2:-1]
    #print(c)
    num=eval(n)
    try:
        i=txt_c.index(c)
        num=num+eval(txt_num[i])
        line=c+"    "+str(num)+"\n"
        txt[i]=line
    except:
        txt.append(line)
    
for i in txt:
    out.write(i)
out.close()

    
    
