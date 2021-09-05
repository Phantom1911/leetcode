#Implementation of Trie DS

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()
        self.endLetter = '*'

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        currentDict = self.root
        for letter in word:
            currentDict = currentDict.setdefault(letter, {})  #checks if the key is present in currentDict, else puts it and sets the value as given value, and returnns it
        currentDict[self.endLetter] = word    #we can make the value as word so we know what it is

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        currentDict = self.root
        for letter in word:
            if letter not in currentDict:
                return False
            currentDict = currentDict[letter]
        if '*' in currentDict:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        currentDict = self.root
        for letter in prefix:
            if letter not in currentDict:
                return False
            currentDict = currentDict[letter]
        return True

if __name__=="__main__":
    obj = Trie()
    obj.insert("word")
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)