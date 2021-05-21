import os

def xiuzheng2(data0,data1):
    Tr=False
    num=data1.count("▲")
    cash=""
    #line=[]
    for n in data0:
        if n=="▲":
            Tr=bool(1-Tr)
        if Tr:
            cash=cash+n 
    cash=cash+"▲"
    if num==2:
        start=data1.index("▲")
        end=data1.index("▲",start+1)
        cash2=""
        for i in range(start,end+1):
            cash2=cash2+data1[i]
        data1=data1.replace(cash2,cash)
    elif num==1:
        start=data1.index("▲")
        data1=data1.replace("▲",cash)   
    elif num==0:
        pos=data0.index("▲")
        if pos/len(data0)<0.5:
            data1=cash+data1
        else:
            data1=data1[:-1]+cash+"\n"
#        print(data1)
    else:
        start=data1.index("▲")
        end0=data1.index("▲",start+1)
        end=data1.index("▲",end0+1)
        cash2=""
        if cash==data1[start:end0+1]:
            for i in range(start,end0+1):
                cash2=cash2+data1[i]
            data1=data1[:end]+data1[end+1:]
            data1=data1.replace(cash2,cash)
        elif cash==data1[end0:end+1]:
            for i in range(end0,end+1):
                cash2=cash2+data1[i]
            data1=data1[:start]+data1[start+1:]
            data1=data1.replace(cash2,cash)
        else:
            for i in range(start,end+1):
                cash2=cash2+data1[i]
            data1=data1.replace(cash2,cash)
    return data1

root=os.getcwd()

lines=""
out=open(root+"/修正sys_text.txt","w+")
f0=open(root+"/sys_jpn.txt",'r')
f1=open(root+"/sys_text2.txt",'r')
f0_lines=f0.readlines()
f1_line=f1.readline()
for f0_line in f0_lines:
    num=f0_line.count("▲")
    if num==2:
        lines=lines+xiuzheng2(f0_line,f1_line)
    elif num==0:
        lines=lines+f1_line.replace("▲","")
    else:
        lines=lines+f1_line
    f1_line=f1.readline()
out.write(lines)
out.close()
