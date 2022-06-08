if __name__=="__main__":

def add(m, c):
    if c in m:
        c[m] += 1
    else:
        c[m] = 1

def minWindow(s, t):
    i,j = 0,0
    have, want = dict(), dict()
    counter = 0   # chars for which condition has been satisfied
    minLen = float("inf")
    for c in t:
        if c in want:
            want[c] += 1
        else:
            want[c] = 1
    while j < len(s):
        add(have, s[j])
        if have[s[j]] == want[s[j]]:
            counter += 1
        if counter == len(want):   # all chars have satisfied property
            minLen = min(minLen, (j-i+1))
            while(counter == len(want)):
                i , counter = incrementStart(i, have, counter, s, want)
                minLen = min(minLen,(j-i+1))

        j += 1

    return minLen

def incrementStart(start, have, counter, s, want):
    have[s[start]] -= 1
    if want[s[start]] < have[s[start]]:
        counter -= 1
    start+=1
    return start, counter




'''
i,j -- x,y

f(i,j) = 1 + min(f(i+2,j+1), f(i-2,j+1), f(i+2, j-1), f(i-2, j-1), ... )

hash(a,b): return a:b
memo[a:b] = minSteps to reach (x,y)
'''
# memo -- O(n^2)
#
# i, j -- i+2, j-1 -- O(n^2)

def hashed(a,b):
    return str(a)+':'+str(b)

def minStepsFunc(i,j , x, y, memo, grid):
    if i == x and j == y:
        return 0
    if hashed(i,j) in memo:
        return memo[hashed(i,j)]
    minSteps = float("inf")
    dirs = [[-2, 1], [-2, -1], [2,1], [2,-1], [-1,2], [-1, -2], [1, -2], [1, 2]]
    for d in dirs:
        a, b = i + d[0], j + d[1]
        if inbounds(a, b, grid):
            minSteps = min(minStepsFunc(a, b, x, y, memo, grid), minSteps) + 1
    memo[hashed(i,j)] = minSteps
    return minSteps

def inbounds(i,j,grid):
    if 0<=i<len(grid) and 0<=j<len(grid[0]):
        return True
    return False

# def f(i,j):
#     if i == x and j == y:
#         return 0
#     if hashed(i,j) in memo:
#         return memo[hashed(i,j)]
#     minSteps = float("inf")
#     dirs = [[-2,1],[2,1] .. ]
#     for d in dirs:
#         a,b = i+d[0] , j+d[1]
#         if inbounds(a,b):
#             minSteps = min(f(a,b), minSteps)+1








