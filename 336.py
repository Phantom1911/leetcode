class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word, index):
        cur_node = self.root

        if self.is_pal(word):
            if 'pal' not in cur_node: cur_node['pal'] = []
            cur_node['pal'] += [index]

        for i, c in enumerate(word):
            if c not in cur_node:
                cur_node[c] = {}
            cur_node = cur_node[c]

            if self.is_pal(word[i + 1:]):
                if 'pal' not in cur_node: cur_node['pal'] = []
                cur_node['pal'] += [index]

        cur_node['end'] = index

    def get(self):
        return self.root

    def is_pal(self, word):
        return word == word[::-1]


class Solution:
    def palindromePairs(self, words):

        trie = Trie()
        empty_word_present = False

        for i, word in enumerate(words):
            trie.insert(word[::-1], i)

        # now check for pairs
        ans = set()

        for index, word in enumerate(words):
            n = len(word)
            cur_node = trie.get()

            # handle empty words
            if 'end' in cur_node and trie.is_pal(word):
                if cur_node['end'] != index: ans.add((index, cur_node['end']))

            word_traversal_complete = True
            for i in range(n):
                c = word[i]

                if c in cur_node:
                    cur_node = cur_node[c]

                else:
                    # if there is no corresponfing word break,
                    # then we could skip word altogether
                    word_traversal_complete = False
                    break

                # left is large and right is short (ends early)
                if 'end' in cur_node and trie.is_pal(word[i + 1:]):
                    if cur_node['end'] != index: ans.add((index, cur_node['end']))

            # left is small and right has more string, which could be a palindrome
            if word_traversal_complete and 'pal' in cur_node:
                for j in cur_node['pal']:
                    if j != index: ans.add((index, j))

        return ans

if __name__=="__main__":
    print(Solution().palindromePairs(["abcd","dcba","lls","s","sssll"]))