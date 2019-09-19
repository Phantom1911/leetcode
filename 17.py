class Solution:

    def letterCombinations(self, digits):
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def combinations(digits, index, ans):
            if index == len(digits):
                ans.append("")
                return ans
            rec_res = combinations(digits, index + 1, ans)
            curr_res = []
            for item in rec_res:
                values = mapping[digits[index]]
                for value in values:
                    new_item = value + item
                    curr_res.append(new_item)
            return curr_res

        return combinations(digits, 0, [])

if __name__=="__main__":
    s = Solution()
    print(s.letterCombinations("23"))