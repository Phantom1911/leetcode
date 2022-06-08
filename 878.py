class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        lo, hi = 1, n * min(a, b)
        candidate_n = None
        mid = None
        while lo <= hi:
            mid = (lo + hi) // 2  # the potential value of m
            candidate_n = mid // a + mid // b - mid // lcm(a, b)
            if candidate_n == n:
                break
            elif candidate_n > n:
                hi = mid
            else:
                lo = mid
        return mid % (10 ** 9 + 7)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a*b) // (gcd(a, b))

if __name__=="__main__":
    print(Solution().nthMagicalNumber(3,6,4))