class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isWord = False
        self.node = dict()

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        newroot = self.root

        for c in word:
            if newroot.node.get(c) is None:
                child = TrieNode()
                newroot.node[c] = child
            newroot = newroot.node[c]
        newroot.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        newroot = self.root

        for c in word:
            if newroot.node.get(c) is None:
                return False
            else:
                newroot = newroot.node.get(c)
        return True if newroot.isWord == True else False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        newroot = self.root

        for c in prefix:
            if newroot.node.get(c) is None:
                return False
            else:
                newroot = newroot.node.get(c)
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
