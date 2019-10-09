class Solution:
    def findComplement(self, num: int) -> int:

        def toBinary(num):
            ans_rev = ""
            while num > 0:
                ans_rev += str(num % 2)
                print(num % 2, " ans_rev now is")
                num = num // 2
            ans = ""
            for i in range(len(ans_rev) - 1, -1, -1):
                ans += ans_rev[i]
            return ans

        def complement(num):
            ans = ""
            for i in range(len(num)):
                if num[i] == '1':
                    ans += '0'
                else:
                    ans += '1'
            return ans

        def toDecimal(num):
            n = len(num)
            ans = 0
            for i in range(n):
                if num[i] == '1':
                    ans += 2 ** (n - i - 1)
            return ans

        binary = toBinary(num)
        print("binary is ", binary)
        comp = complement(binary)
        print("comp is ", comp)
        ans = toDecimal(comp)
        print("ans ", ans)
        return ans