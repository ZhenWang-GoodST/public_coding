
#CalHamletV1.py
def getText():
    txt = open("D:\desktop\github\ICRA2020-paper-list\index.txt", "r").read()   #读取Hamlet文本文件，并返回给txt
    txt = txt.lower()          #将文件中的单词全部变为小写
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~': 
        txt = txt.replace(ch, " ")   #将文本中特殊字符替换为空格
    return txt
 
hamletTxt = getText()
words  = hamletTxt.split() #按照空格，将文本分割
counts = {}
for word in words:  #统计单词出现的次数，并存储到counts字典中         
    counts[word] = counts.get(word,0) + 1  #先给字典赋值，如果字典中没有word这个键，则返回0；见下面函数讲解
items = list(counts.items())   #将字典转换为列表，以便操作
items.sort(key=lambda x:x[1], reverse=True)  # 见下面函数讲解
print(len(items))
for i in range(10):
    word, count = items[i]
    #print ("{0:<10}{1:>5}".format(word, count))
fo = open("D:\desktop\github\\notebooks\paper_collection_and_management\statistics.txt", "w")
print(len(items))
for i in range(len(items)):
    word, count = items[i]
    #print ("{0:<10}{1:>5}".format(word, count))
    fo.write( "{0:<10}{1:>5}".format(word, count)+"\n")
 
# 关闭打开的文件
fo.close()