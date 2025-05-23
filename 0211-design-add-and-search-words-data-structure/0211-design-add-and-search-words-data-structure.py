class Node:
    def __init__(self, ending = False):
        self.children = {}
        self.ending = ending

class WordDictionary(object):

    def __init__(self):
        self.root = Node()
    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.ending = True
    
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(node, index):
            if index == len(word):
                return node.ending
            char = word[index]
            if char == ".":
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], index + 1)
        return dfs(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)    