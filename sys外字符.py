import os

fre=open("总字频.txt","r")
sys=open("sys_字频2.txt","r")
lookup=open("orlookup的副本.txt",'r')
char=open("char映射.txt",'r')
#orl=open("orlookup.txt",'r')
#lookup=orl.readlines()
fre=fre.readlines()
sys=sys.readlines()
c_data=[]
for line in sys:
    c_data.append(line[0])
for line in fre:
    c=line[0]
    try:
        i=c_data.index(c)
    except:
        print(c)
        #不包含在系统文本里的字符

print("\n-----------\n")
lookup=lookup.readlines()
char=char.readlines()
c_data=[]
for line in lookup:
    c_data.append(line[0])
for line in char:
    c=line[0]
    try:
        i=c_data.index(c)
    except:
        print(c)
        #不包含在lookup里的字库字符
        
print("\n-----------\n")
c_data=[]
for line in char:
    c_data.append(line[0])
for line in lookup:
    c=line[0]
    try:
        i=c_data.index(c)
    except:
        print(c)
        #不包含在映射表的lookup字符
