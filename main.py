from PinyinDict import pinyinDict
from PinyinDict import is_Chinese
from pypinyin import lazy_pinyin
from Ngram import get2grams
filename = 'data.txt'
f = open("data.txt", 'r', encoding='UTF-8').read()
res = ""
str_pin = []
str_word = []
for i in f:
    if is_Chinese(i):
        res += i
        str_word += i
        str_pin += lazy_pinyin(i)
input_learn = []
print(11)
for c in res:
    input_learn.append(c)
# 字和字之间的2-gram
ngram = get2grams(str_word)
# 拼音和字的配对,字典树
pd, tree = pinyinDict(input_learn)
# 转移概率，初始概率
# 整段读入所以初始字只有一个
print(pd)
print(ngram)
result = []
result += "迈"
sum = 0
error = 0
ff = open("data_test", 'r', encoding='UTF-8').read()
test_word = []
test_pin = []
for i in ff:
    if is_Chinese(i):
        res += i
        test_word += i
        test_pin += lazy_pinyin(i)
for i in range(len(test_pin) - 1):
    p = {}
    max_p = 0
    first_w = result[i]
    last_p = test_pin[i+1]
    flag = 0
    for kk in pd[last_p]:
        if kk in ngram[first_w]:
            flag = 1
            # print(kk)
            p[kk] = pd[last_p][kk] * ngram[first_w][kk]
            if p[kk] > max_p:
                index = kk
                max_p = p[kk]
    if flag == 0:
        for kk in pd[last_p]:
            p[kk] = pd[last_p][kk]
            if p[kk] > max_p:
                index = kk
                max_p = p[kk]
    # print(index)
    result += index
    if index != test_word[i+1]:
        error += 1
print(result)
print("测试文本字数：")
print(len(result))
print("正确率为：")
print(1 - error/len(result))

