from xml.dom.minidom import parse
import os

def readXML():
    domTree = parse(path2)
    rootNode = domTree.documentElement
    Dialog = rootNode.getElementsByTagName("Dialog")
    for Dia in range(len(Dialog)):
        Text=rootNode.getElementsByTagName('Dialog')[Dia].childNodes[0].nodeValue
        Text=Text.replace('\n','')
        new_context = Text + '\n'
        f.write(new_context)

root="/Users/zhaochen/Downloads/NLPP汉化/NLPPGit-master/NLPP_scripts-Need_clean_translation"

path=os.getcwd()
for file in os.listdir(root):
    path2=root+"/"+file
    name=file.split(".")[0]+".txt"
    print(name)
    f=open(path+"/Text/JPN/"+name, "w")
    readXML()
    f.close()
