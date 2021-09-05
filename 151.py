class Solution:
    def groupAnagrams(self, strs) :
        mapper = dict()
        for word in strs:
            key = ''.join(sorted(word))
            if key in mapper:
                mapper[key].append(word)
            else:
                mapper[key] = []
                mapper[key].append(word)

        res = []
        for key in mapper:
            res.append(mapper[key])
        return res

if __name__=="__main__":
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))