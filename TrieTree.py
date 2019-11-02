class Node:
    def __init__(self, name):
        self.name = name
        self.son = {}
        self.fre = 0
        self.end = False
        self.root = False

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def set_son(self, son):
        self.son = son

    def get_son(self):
        return self.son

    def get_fre(self):
        return self.fre

    def set_fre(self, num):
        self.fre = num

    def get_end(self):
        return self.end

    def set_end(self, end):
        self.end = end

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root


class TrieTree:
    def __init__(self, name):
        self.root = Node(name)
        self.root.set_end(False)
        self.root.set_fre(0)
        self.root.set_root(True)

    def insert(self, word):
        node = self.root
        words = []
        for c in word:
            words.append(c)
        for i in range(len(words)):
            if words[i] in node.get_son():
                if i == len(words)-1:
                    end_node = node.get_son()[words[i]]
                    end_node.set_fre(end_node.get_fre() + 1)
                    end_node.set_end(True)
            else:
                new_node = Node(words[i])
                if i == len(words) - 1:
                    new_node.set_fre(1)
                    new_node.set_end(True)
                    new_node.set_root(False)
                node.get_son()[words[i]] = new_node
            node = node.get_son()[words[i]]

    def search(self, word):
        fre = -1
        node = self.root
        words = []
        for c in word:
            words.append(c)
        for i in range(len(words)):
            # 若找到了就到单词结尾
            if words[i] in node.get_son():
                node = node.get_son()[words[i]]
                fre = node.get_fre()
            # 若没找到直接返回
            else:
                fre = -1
                pass
        return fre

    def split_spell(self, spell):
        node = self.root
        words = []
        for c in spell:
            words.append(c)
        spells = ''
        i = 0
        while i < len(words)-1:
            # print(i)
            # print(spells)
            # print(words[i])
            if words[i] in node.get_son():
                # print(words[i])
                spells += words[i]
                node = node.get_son()[words[i]]
                i = i + 1
            else:

                node = self.root
                spells = spells + " "
                # i = i - 1

        spells += words[len(words)-1]
        # print(spells)
        return spells


'''
tree = TrieTree('test')
tree.insert('gao')
tree.insert('wo')
tree.insert('xing')
tree.split_spell('wogaoxing')
'''
