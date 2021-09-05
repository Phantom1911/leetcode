def multiStringSearch(bigString, smallStrings):
    # Write your code here.
    # construct a trie using all the smaller strings
    trie = Trie()
    all_lengths = set()
    for s in smallStrings:
        trie.insert(s)
        all_lengths.add(len(s))
    word_indices = dict()
    for i in range(len(smallStrings)):
        word_indices[smallStrings[i]] = i

    output = [False for i in range(len(smallStrings))]
    for i in range(len(bigString)):
        for length in all_lengths:
            if i + length < len(bigString) - 1:
                currSubstring = bigString[i:i + length]
                if trie.isPresent(currSubstring):
                    idx = word_indices[currSubstring]
                    output[idx] = True

    return output


# every level in the trie DS is a dict
class Trie:
    def __init__(self):
        self.root = dict()
        self.endLetter = '*'

    def insert(self, word):
        currentDict = self.root
        for letter in word:
            currentDict = currentDict.setdefault(letter, {})
        currentDict[self.endLetter] = word

    def isPresent(self, word):
        currentDict = self.root
        for letter in word:
            if letter in currentDict:
                currentDict = currentDict[letter]
            else:
                return False
        if self.endLetter in currentDict:
            return True
        return False

if __name__=="__main__":
    bigString = "this is a big string"
    smallStrings = ["this", "is", "not"]
    print(multiStringSearch(bigString, smallStrings))