import string
from matplotlib import pyplot as plt

def process_line(line,hist):
    line = line.replace('-',' ')
    #分割每一行
    for word in line.split():
        #去掉标点符号（只去掉收尾的）
        word=word.strip(string.punctuation + string.whitespace)
        #统一大小写
        word = word.lower()
        #加入word中
        hist[word] = hist.get(word,0) + 1


def process_file(filename):
    hist = {}
    with open(filename,'r') as f:
        for line in f:
            process_line(line,hist)
    return  hist

def most_common(hist,num):
    #获取前N个单词
    t = []
    #循环字典中的每一个key和value
    for key,value in hist.items():
        t.append((value,key))
    #反向排序
    t.sort(reverse=True)

    return t[:num]


def run():
    hist = process_file('emma.txt')
    #print(hist)
    #获取topN
    data = most_common(hist,3)
    print(data)

    for word in data:
        plt.bar(word[-1:],word[:1])
    '''
    plt.bar(('false','lalala'),(10,))
    plt.bar(('sucess',),(5,))
    plt.bar(('beautiful',),(5,))
    '''
    plt.legend()
    plt.xlabel('words')
    plt.ylabel('rate')
    plt.title('xxxx')
    plt.show()
    print(word[-1:])


if __name__ == '__main__':
    run()

#单词的总长度
#print(len(words))
