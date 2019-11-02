from PinyinDict import pinyinDict
from PinyinDict import is_Chinese
from learn import learn
from pypinyin import lazy_pinyin
from Ngram import get2grams
import numpy as np
# 拼音切割的实例
pinyinString = "maixiangchongmanxiwangdexinshiji"
filename = 'data_trie'
f = open(filename, 'r', encoding='UTF-8').read()
res = ""
str_pin = []
str_word = []
for i in f:
    if is_Chinese(i):
        res += i
        str_word += i
        str_pin += lazy_pinyin(i)
input_learn = []
for c in res:
    input_learn.append(c)
# 字和字之间的2-gram
ngram = get2grams(str_word)
# 拼音和字的配对,字典树
pd, tree = pinyinDict(input_learn)
obs = tree.split_spell(pinyinString).split(" ")
print(pinyinString)
print(obs)
