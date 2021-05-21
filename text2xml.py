from xml.dom.minidom import parse
import os, xml.dom.minidom
from xml.etree.ElementTree import ElementTree,Element
import xml.etree.ElementTree as ET

def readXML():
    domTree = parse(pathxml+"/"+file)
    rootNode = domTree.documentElement
    Dialog = rootNode.getElementsByTagName("Dialog")
    for Dia in range(len(Dialog)):
        Text = t.readline()
        Text = Text.replace("\n",'')
        rootNode.getElementsByTagName('Dialog')[Dia].childNodes[0].data=Text
    with open(pathout+file, 'w') as f:
        # 缩进 - 换行 - 编码
        domTree.writexml(f, addindent='  ', encoding='utf-8')

path=os.getcwd()+"/Text/nene_映射标号/"
pathxml=os.getcwd()+"/xml/NLPP"
pathout=os.getcwd()+"/xml/标号/"
for file in os.listdir(pathxml):
    if file.split(".")[-1]=="xml":
        try:
            t = open(path+file.replace("xml","txt"))
            readXML()
            t.close()
        except:
            print(file)
print('写入OK!')

