def patternMatcher(pattern, string):
    noOfX = 0
    noOfY = 0
    lenPat = len(pattern)
    lenStr = len(string)
    for i in range(lenPat):
        if pattern[i] == 'x':
            noOfX += 1
        else:
            noOfY += 1

    # iterate for different lengths of x
    for i in range(1, lenStr + 1):
        if noOfY != 0:
            lenY = int((lenStr - (noOfX * i)) / noOfY)
            if lenY < 0:
                break
        if pattern[0] == 'x':
            x = string[:i]
            j = 0
            while j < lenPat and pattern[j] != 'y':
                j += 1
            if j == lenPat:
                y = ''
            else:
                offset = j * len(x)
                y = string[offset : (offset + lenY)]
        else:
            y = string[:lenY]
            j = 0
            while j < lenPat and pattern[j] != 'x':
                j += 1
            if j == lenPat:
                x = ''
            else:
                offset = j * len(y)
                x = string[offset:offset + i]
        currStr = ''
        for k in range(lenPat):
            if pattern[k] == 'x':
                currStr += (x)
            else:
                currStr += (y)
        if currStr == string:
            return [x, y]

    return []


if __name__=="__main__":
    print(patternMatcher("xxxx", "testtesttesttest"))