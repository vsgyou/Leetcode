class Node:
    def __init__(self, ending = False):
        self.children = {}
        self.ending = ending
class Trie(object):

    def __init__(self):
        self.root = Node(ending = True)

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for chr in word:
            if chr not in node.children:
                node.children[chr] = Node()
            node = node.children[chr]
        node.ending = True


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for chr in word:
            if chr not in node.children:
                return False
            node = node.children[chr]
        return node.ending


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for chr in prefix:
            if chr not in node.children:
                return False
            node = node.children[chr]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)