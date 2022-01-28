class Solution:
    def maxValue(self, n: str, x: int) -> str:
        # if n is negative, then make smallest magnitude
        # if n is positive, then make largest magnitude
        isneg = True if n[0] =='-' else False
        if not isneg:
            m = 0
            while m < len(n) and x <= int(n[m]):
                m += 1
            print(m)
            return n[0:m]+str(x)+n[m:]
        else:
            m = 0
            n = n[1:]
            while m < len(n) and x >= int(n[m]):
                m += 1
            print(m)
            return "-"+n[0:m]+str(x)+n[m:]