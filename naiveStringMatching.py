def stringMatcher(string, pattern):
    n = len(string)
    m = len(pattern)
    for i in range(n-m+1):
        j , k = 0, i
        while j < m:
            if pattern[j] == string[k]:
                j+=1
                k+=1
            else:
                break
        if j == k-i and j == m:
            return "yes"
    return "no"

if __name__=="__main__":
    print(stringMatcher("abcdef", "cd"))
