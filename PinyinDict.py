from pypinyin import lazy_pinyin
from TrieTree import TrieTree


def is_Chinese(word):

    for ch in word:

        if '\u4e00' <= ch <= '\u9fff':

            return True

    return False


# 将文字和拼音构成词典
# 拼音 -- {字 - fre}
def pinyinDict(input):
    str = []
    tree = TrieTree('tree')
    output = {}
    for i in range(len(input)):
        if is_Chinese(input[i]):

            pinyin = lazy_pinyin(input[i])[0]
            str += pinyin
            if pinyin not in output:
                output[pinyin] = {}
                tree.insert(pinyin)
            if input[i][0] not in output[pinyin]:
                output[pinyin][input[i][0]] = 0
            output[pinyin][input[i][0]] += 1
    for k in output:
        sum = 0
        for kk in output[k]:
            sum += output[k][kk]
        for kk in output[k]:
            output[k][kk] /= sum
    # print(str)
    return  output, tree


'''
x = ["我", "去", "上", "学"]
print(pinyinDict(x))
'''
