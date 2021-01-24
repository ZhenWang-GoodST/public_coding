#!/usr/bin/python3 # 第一个注释
import sys

#print(sys.argv[0])
#print(sys.argv[1])
#print(len(sys.argv))

path = sys.argv[1]
input_file = path + "\\" + sys.argv[2] + ".txt"
output_file = path + "\\" + sys.argv[3] + ".txt"
#output_fileName = path + sys.argv[2] + "_" + str_name + ".txt"

print("input_file: " + input_file )
print("output_file: " + output_file )
#print("output_file: " + output_fileName )

def getText(input_file):
    #origin_txt = open(input_file, "r",encoding='gbk').read()#gbk
    origin_txt = open(input_file, "rb").read()
    origin_txt = origin_txt.decode()
    #for ch in '!"#$%&()*+,./:;<=>?@[\\]^_‘{|}~': 
    #    origin_txt = origin_txt.replace(ch, " ")   #将文本中特殊字符替换为空格
    return origin_txt

origin_txt = getText(input_file)
origin_papers = origin_txt.split("\n")
str_papers = []
isKey = False
fo = open(output_file, "wb")
fo.write("".encode())
fo.close()
fo = open(output_file, "wb+")
keywords = ""
line_content = ""
writeline = False
paper_count = 0
keywords_count = 0
abstract_count = 0
i = 0
while i < len(origin_papers):
    line = origin_papers[i]
    writeline = False
    if line.startswith("TI  - "):
        #fo.write(line + "\n")
        line = line.replace("TI  - ", "Title: ")
        line_content = line + "\n"
        writeline = True
        paper_count += 1
    if line.startswith("KW  - ") and isKey == False:
        line = line.replace("KW  - ", "Key Words: ")
        line = line.replace("\r", " ")
        keywords = line
        isKey = True
        #print("key words\n")
        while isKey == True:
            i = i + 1;
            line = origin_papers[i]
            if line.startswith("KW  - ") and isKey == True:
                line = line.replace("KW  - ", " ")
                line = line.replace("\r", " ")
                keywords += line
            else:
                isKey = False
                line_content = keywords + "\n"
                writeline = True
                keywords_count += 1
                #fo.write(keywords + "\n")
    if line.startswith("AB  - "):
        line = line.replace("AB  - ", "Abstract: ")
        line_content = line + "\n\n"
        writeline = True
        abstract_count += 1
        #fo.write(line + "\n\n")
        if paper_count!=abstract_count:
            j = 1
            print(line)
    if writeline:
        fo.write(line_content.encode())
    i = i + 1
    

print("paper_count: " +str(paper_count))
print("keywords_count: " +str(keywords_count))
print("abstract_count: " +str(abstract_count))

fo.close()
i = 1



