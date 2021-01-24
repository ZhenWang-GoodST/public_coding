#!/usr/bin/python3 
# coding=utf-8
import os

filePath = "D:\\desktop\\github\\notebooks\\paper_list\\IROS2018"
outpath = "D:\\desktop\\github\\notebooks\\paper_list\\IROS2018\\IROS2018.txt"
def readname():

    name = os.listdir(filePath)
    return name

files = readname()
count = 0
papers = []
for file in files:
    filepath = filePath + "\\" + file
    text = open(filepath, "rb").read()#字符类型gbk处理不了，当做二进制
    #从str到bytes:调用方法encode().
    #从bytes到str:调用方法decode().
    lines = text.decode()
    lines = lines.split("\n")
    for line in lines:
        #print(line)
        if line.startswith("TI  - "):
            line.replace("TI  - ", " ")
            papers.append("  " + line[6:] + "\n" )
            count += 1

fo = open(outpath, "wb")
string = "total " + str(count) + " papers" + "\n"
string = string.encode()
fo.write(string)
for paper in papers:
    fo.write(paper.encode())
fo.close()
print(count)



