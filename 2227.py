from typing import List


class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.keys = keys
        self.values = values
        self.dictionary = dictionary
        self.map1 = self.buildMap(keys)
        self.map2 = self.getEncryptedWords(dictionary)

    def encrypt(self, word1: str) -> str:
        ans = ''
        for c in word1:
            strToAdd = ''
            if c in self.map1:
                idxInKeys = self.map1[c]
                strToAdd = self.values[idxInKeys]
            else:
                return ''
            ans += strToAdd
        return ans

    def decrypt(self, word2: str) -> int:
        count = 0
        for key in self.map2:
            if self.map2[key] == word2:
                count += 1
        return count

    def buildMap(self, keys):
        m = {}
        for i in range(len(keys)):
            # which index each character is present at
            m[keys[i]] = i
        return m

    def getEncryptedWords(self, dictionary):
        m = {}
        for word in dictionary:
            m[word] = self.encrypt(word)
        return m


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)

if __name__=="__main__":
    keys = ["a", "b", "c", "d"]
    values = ["ei", "zf", "ei", "am"]
    dictionary = ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]
    word1 = 'abcd'
    word2 = 'eizfeiam'
    obj = Encrypter(keys, values, dictionary)
    param_1 = obj.encrypt(word1)
    param_2 = obj.decrypt(word2)

# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)