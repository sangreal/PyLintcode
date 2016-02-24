class TrieNode(object):
    def __init__(self):
        self.wordlist = [None for x in xrange(26)]
        self.isWord = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        if len(word) == 0:
            return

        curNode = self.root
        for i in xrange(len(word)):
            idx = ord(word[i])-ord('a')
            if curNode.wordlist[idx] is None:
                curNode.wordlist[idx] = TrieNode()
            curNode = curNode.wordlist[idx]

        curNode.isWord = True

    def search(self, word, curNode):
        if curNode is None: return False

        if len(word) == 0:
            if curNode.isWord: return True
        else: return False

        if word[0] == '.':
            for nextNode in curNode.wordlist:
                if self.search(word[1:], nextNode):
                    return True
        else:
            idx = ord(word[0])-ord('a')
            return self.search(word[1:], curNode.wordlist[idx])

        return False


    def startwith(self, word):

        curNode = self.root
        for item in word:
            if item == '.':
                return True
            idx = ord(item)-ord('a')
            if curNode.wordlist[idx] is None:
                return False
            else:
                curNode = curNode.wordlist[idx]
        return curNode.isWord



class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.trie.addWord(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.trie.search(word, self.trie.root)