#!/usr/bin/python3 # 第一个注释
import sys

#print(sys.argv[0])
#print(sys.argv[1])
print(len(sys.argv))

path = sys.argv[1]
input_fileName = path + "\\" + sys.argv[2] + ".txt"
str_name = sys.argv[3]
with_key_words = True
if len(sys.argv) > 4:
    with_key_words = sys.argv[4]
    key_words = "key_words: "
else:
    key_words = "key words: "


print("get paper list contains: " +str_name )
print("input_file: " + input_fileName )

def getText(input_file):
    #origin_txt = open(input_file, "r",encoding='gbk').read()#gbk
    origin_txt = open(input_file, "rb").read()
    origin_txt = origin_txt.decode()
    lower_txt = origin_txt.lower()          #将文件中的单词全部变为小写
    for ch in '!"#$%&()*+,./;<=>?@[\\]^_‘{|}~': 
        #origin_txt = origin_txt.replace(ch, " ")   #将文本中特殊字符替换为空格
        lower_txt = lower_txt.replace(ch, " ")
    return origin_txt,lower_txt

origin_txt,lower_txt = getText(input_fileName)
origin_papers = origin_txt.split("\n")
lower_papers = lower_txt.split("\n")
str_papers = []
lower_str_name = str_name.lower()
i = 0
title = ""
keywords = ""
abstract = ""
title_id = 0
keywords_id = 0
abstract_id = 0
length = len(lower_papers)
count = 0

while i < len(lower_papers):
    line = lower_papers[i]
    if line.startswith("title: "):
        title_id = i
        title = line.replace("title: " , "") + "\n"
    if line.startswith(key_words):
        keywords_id = i
        keywords = line.replace("key words: " , "") + "\n"
    if line.startswith("abstract: "):
        abstract_id = i
        abstract = line.replace("abstract: " , "") + "\n\n"
        find_words = title + keywords + abstract
        if lower_str_name in find_words :
            paper = origin_papers[title_id] + "\n" + origin_papers[keywords_id] + "\n" +origin_papers[abstract_id] + "\n\n"
            if len(sys.argv) > 4:
                paper = origin_papers[title_id] + "\n" +origin_papers[abstract_id] + "\n\n"
            else:
                paper = origin_papers[title_id] + "\n" + origin_papers[keywords_id] + "\n" +origin_papers[abstract_id] + "\n\n"
            #paper = "Title: " + title + "Keywords: " + keywords + "Abstract: " + abstract
            str_papers.append(paper)
            #print(paper)
            count += 1
    i += 1
print(count)
length_string = str(len(str_papers))
output_fileName = path + "\\" + str_name  + "_" + length_string + "_" + sys.argv[2] + ".txt"
if len(sys.argv) > 4:
    output_fileName = path + "\\" + "noKey_" + str_name  + "_" + length_string + "_" +  sys.argv[2] + ".txt"
    
fo_out = open(output_fileName, "wb")
#fo_out = open(output_fileName, "w",encoding='gbk')#gbk
#fo_out.write( "total paper: " + str(len(str_papers)) + "\n")#gbk
fo_out.write( ("total paper: " + str(len(str_papers)) + "\n").encode())
for i in range(len(str_papers)):
    #print ("{0:<10}{1:>5}".format(word, count))
    #fo_out.write( str_papers[i] + "\n")#gbk
    fo_out.write( (str_papers[i] + "\n").encode())
 
fo_out.close()

