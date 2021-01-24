#!/usr/bin/python3 # 第一个注释
import sys

#print(sys.argv[0])
#print(sys.argv[1])
#print(len(sys.argv))

path = sys.argv[1]
input_fileName = path + sys.argv[2] + ".txt"
str_name = sys.argv[3]
#output_fileName = path + sys.argv[2] + "_" + str_name + ".txt"

print("get paper list contains: " +str_name )
print("input_file: " + input_fileName )
#print("output_file: " + output_fileName )

def getText(input_file):
    #origin_txt = open(input_file, "r",encoding='gbk').read()#gbk
    origin_txt = open(input_file, "rb").read()
    origin_txt = origin_txt.decode()
    lower_txt = origin_txt.lower()          #将文件中的单词全部变为小写
    for ch in '!"#$%&()*+,./:;<=>?@[\\]^_‘{|}~': 
        origin_txt = origin_txt.replace(ch, " ")   #将文本中特殊字符替换为空格
        lower_txt = lower_txt.replace(ch, " ")
    return origin_txt,lower_txt

origin_txt,lower_txt = getText(input_fileName)
origin_papers = origin_txt.split("\n")
lower_papers = lower_txt.split("\n")
str_papers = []
lower_str_name = str_name.lower()
for i in range(len(lower_papers)):
    if lower_str_name in lower_papers[i] :
        str_papers.append(origin_papers[i])
        j = i + 1

length_string = str(len(str_papers))
output_fileName = path + sys.argv[2] + "_" + str_name + "_" + length_string + ".txt"
fo_out = open(output_fileName, "wb")
#fo_out = open(output_fileName, "w",encoding='gbk')#gbk
#fo_out.write( "total paper: " + str(len(str_papers)) + "\n")#gbk
fo_out.write( ("total paper: " + str(len(str_papers)) + "\n").encode())
for i in range(len(str_papers)):
    #print ("{0:<10}{1:>5}".format(word, count))
    #fo_out.write( str_papers[i] + "\n")#gbk
    fo_out.write( (str_papers[i] + "\n").encode())
 
fo_out.close()
