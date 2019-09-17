class subsequences:
    def all_subsequences(self, s, index, ans):
        if index == len(s):
            ans.append("")
            return ans
        rec_res = self.all_subsequences(s, index+1, ans)
        curr_res = []
        for item in rec_res:
            curr_item = s[index]+item
            curr_res.append(curr_item)
            curr_res.append(item)
        return curr_res
if __name__=="__main__":
    s = subsequences()
    print(s.all_subsequences("abc", 0, []))