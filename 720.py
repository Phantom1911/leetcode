class Solution:
    def longestWord(self, words) :
        trie = Trie()
        for word in words:
            trie.insert(word)
        maxword, maxwordlen = None, 0
        for word in words:
            if trie.searchIncremental(word) and len(word) == maxwordlen:
                maxword = word if word < maxword else maxword
            elif trie.searchIncremental(word) and len(word) > maxwordlen:
                maxword, maxwordlen = word, len(word)
        return maxword


class Trie:
    def __init__(self):
        self.root = {}
        self.endletter = '*'

    def insert(self, word):
        currentDict = self.root
        for letter in word:
            if letter not in currentDict:
                currentDict[letter] = {}
            currentDict = currentDict[letter]
        currentDict[self.endletter] = word  # we can make the value as word so that we know what it is

    def searchIncremental(self, word):
        currentDict = self.root
        for letter in word:
            if letter in currentDict:
                currentDict = currentDict[letter]
            else:
                return False
            if self.endletter not in currentDict:
                return False

        if self.endletter not in currentDict:
            return False
        return True

if __name__=="__main__":
    print(Solution().longestWord(["w","wo","wor","worl","world"]))