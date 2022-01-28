class Solution:
    def generate_binary_string(self,s):
        ans = []
        flag = False
        for i in range(len(s)):
            if s[i] == '?':
                flag = True
                # replace with '0'
                remstrs = self.generate_binary_string(s[i+1:])
                for st in remstrs:
                    ans.append(s[0:i]+'0'+st)
                    ans.append(s[0:i] + '1' + st)
                break
        if flag == False:
            return [s]
        return ans

if __name__=="__main__":
    print(Solution().generate_binary_string('1??0?101'))