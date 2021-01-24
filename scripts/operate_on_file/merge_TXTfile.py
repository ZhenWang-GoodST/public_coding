
#!/usr/bin/python3 # 第一个注释
import sys
import os

#directory path
#output file name
path = sys.argv[1]
output_name = path + "\\" + sys.argv[2] + ".txt"

print("path: " +path )
print("output_name: " + output_name )

def readname(dirPath):

    name = os.listdir(dirPath)
    return name

files = readname(path)
fo = open(output_name,"wb+")
#text = ""
for file in files:
    filepath = path + "\\" + file
    text = open(filepath, "rb").read()#字符类型gbk处理不了，当做二进制
    #从str到bytes:调用方法encode().
    #从bytes到str:调用方法decode().
    fo.write(text)
fo.close()
