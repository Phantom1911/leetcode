class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = []
        for w in words:
            masks.append(self.create_mask(w))
        ans = 0
        for i in range(len(words) + 1):
            for j in range(i + 1, len(words)):
                if masks[i] & masks[j] == 0:
                    if len(words[i]) * len(words[j]) > ans:
                        ans = len(words[i]) * len(words[j])

        return ans

    def create_mask(self, str):
        mask = 0
        for c in str:
            mask |= 1 << (ord(c) - ord('a'))
        return mask