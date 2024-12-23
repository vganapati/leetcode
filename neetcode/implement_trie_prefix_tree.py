"""
https://neetcode.io/problems/implement-prefix-tree
https://leetcode.com/problems/implement-trie-prefix-tree/description/
"""

class TreeNode:
    def __init__(self, val=None, children=None, word_end=False):
        self.val = val
        self.children = children
        self.word_end = word_end


class Trie:
    def __init__(self):
        self.head = TreeNode(children={})
    def insert(self, word: str) -> None:
        node = self.head
        for ind, char in enumerate(word):
            if char in node.children.keys():
                node = node.children[char]
            else:
                node.children[char] = TreeNode(children={})
                node = node.children[char]
            if ind == len(word)-1:
                node.word_end = True
    def search(self, word: str) -> bool:
        node = self.head
        for char in word:
            if char in node.children.keys():
                node = node.children[char]
            else:
                return False
        return node.word_end
    def startsWith(self, prefix: str) -> bool:
        node = self.head
        for char in prefix:
            if char in node.children.keys():
                node = node.children[char]
            else:
                return False
        return True

my_trie = Trie()
my_trie.insert("apple")
assert my_trie.search("apple") == True
assert my_trie.search("app") == False
assert my_trie.startsWith("app") == True
my_trie.insert("app")
assert my_trie.search("app") == True

my_trie = Trie()
assert my_trie.startsWith("a") == False