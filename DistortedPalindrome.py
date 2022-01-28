# https://www.codechef.com/problems/ENCD12

# each swap is identified uniquely by an index pair. there are n different swap pairs possible, which will result in n! paths
# follow each path by swapping, checking if it's a palindrome at each step
# return min swaps if we get palindrome , else return "impossible"

def minadjswaps(s):
    swappairs = []
    for i in range(0,len(s)-1, 1):
        swappairs.append((i,i+1))
    perms = permutations(swappairs)

    for perm in perms:
        count = 0
        for i in range(len(perm)):
            currswap = perm[i]


def permutations(arr):




if __name__=="__main__":
    while True:
        s = input()
        if s == '0':
            break
        print(minadjswaps(s))
