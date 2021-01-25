#!/usr/bin/python3 # 第一个注释
import sys

#print(sys.argv[0])
#print(sys.argv[1])
print(len(sys.argv))

path = sys.argv[1]
input_fileName = path + "\\" + sys.argv[2] + ".txt"
with_key_words = True
with_abstract = True
with_key_words = int(sys.argv[3])
with_abstract= int(sys.argv[4])
if with_key_words == False:
    key_words = "key_words: "
else:
    key_words = "key words: "
if with_abstract == False:
    abstract_words = "abstract1: "
else:
    abstract_words = "abstract: "

str_names = []
i = 5
out_str_name = ""
while i < len(sys.argv):
    str_names.append(sys.argv[i].lower())
    out_str_name += sys.argv[i].lower() + "_"
    i += 1

print("get paper list contains: "  )
print(str_names)
print("input_file: " + input_fileName )
print("with keywords: " + str(with_key_words))
print("with abstract: " + str(with_abstract))

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
i = 0
title = ""
keywords = ""
abstract = ""
title_id = 0
keywords_id = 0
abstract_id = 0
length = len(lower_papers)
count = 0
one_title = False
find_words = ""
while i < len(lower_papers):
    line = lower_papers[i]
    if line.startswith("title: "):
        title_id = i
        title = line.replace("title: " , "") + "\n"
    if line.startswith(key_words):
        keywords_id = i
        keywords = line.replace("key words: " , "") + "\n"
    if line.startswith(abstract_words):
        abstract_id = i
        abstract = line.replace(abstract_words , "") + "\n\n"
    if line == "":#one paper
        in_find_words = True
        find_words = title + keywords + abstract
        for str_name in str_names:
            if str_name not in find_words:
                in_find_words = False
        if in_find_words:
            paper = origin_papers[title_id] + "\n"
            if with_key_words:
                paper += origin_papers[keywords_id] + "\n"
            if with_abstract:
                paper += origin_papers[abstract_id] + "\n"
            paper += "\n"
            str_papers.append(paper)
            #print(paper)
            count += 1
        title = ""
        keywords = ""
        abstract = ""
    i += 1
print(count)
length_string = str(len(str_papers))
output_fileName = path + "\\" + out_str_name + length_string
if with_key_words:
    output_fileName += "_keyWord" 
if with_abstract:
    output_fileName += "_abstract" 
output_fileName += "_" +  sys.argv[2] + ".txt"
fo_out = open(output_fileName, "wb")
#fo_out = open(output_fileName, "w",encoding='gbk')#gbk
#fo_out.write( "total paper: " + str(len(str_papers)) + "\n")#gbk
fo_out.write( ("total paper: " + str(len(str_papers)) + "\n").encode())
for i in range(len(str_papers)):
    #print ("{0:<10}{1:>5}".format(word, count))
    #fo_out.write( str_papers[i] + "\n")#gbk
    fo_out.write( (str_papers[i] + "\n").encode())
 
fo_out.close()
