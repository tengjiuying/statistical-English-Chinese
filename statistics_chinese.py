import jieba

with open('三国演义.txt','r',encoding='GB18030') as f:
    content = f.read()

res = jieba.lcut(content)
#print(res)
hist = {}

for word in res:
    if len(word) == 1:
        continue
    if word in hist:
        hist[word] = hist[word] + 1
    else:
        hist[word] = 1

#排序：将字典变为列表来排序
hist = list(hist.items())
#key代表按照hist元素中的索引为数字的进行排序
hist.sort(key=lambda x:x[1],reverse=True)

#格式输出 输出前15个

for i in range(15):
    #等价于
        #word=hist[i][0]
        #count=hist[i][1]
    word,count = hist[i]
    #左对齐10个，右对齐5个
    print("{:<10}{:>5}".format(word,count))



#print(hist)