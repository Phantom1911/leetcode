class Solution:
    def isNumber(self, s: str) -> bool:
        containsE, containse = False, False
        for i in range(len(s)):
            if (s[i] == 'E' and containsE) or (s[i] == 'E' and containse):
                return False
            elif (s[i] == 'e' and containsE) or (s[i] == 'e' and containse):
                return False
            elif s[i] == 'e':
                containse = True
            elif s[i] == 'E':
                containsE = True
        if containsE and containse:
            return False
        arr = None
        if containsE :
            arr = s.split("E")
        elif containse:
            arr = s.split("e")
        if containsE or containse:
            if (isDec(arr[0]) and isInt(arr[1])) or (isInt(arr[0]) and isInt(arr[1])):
                return True
            return False
        else:
            print("hi")
            print("isdec" + str(isDec(s)))
            return isDec(s) or isInt(s)

def isDec(s):
    if len(s) == 0:
        return False
    if s[0] != '.' and s[0] != '-' and s[0] != '+' and not (48 <= ord(s[0]) <= 57):
        print("3")
        return False
    if s[-1] == '-' or s[-1] == '+':
        print("4")
        return False
    if len(s) == 1 and not (48 <= ord(s[0]) <= 57):
        return False
    if s[0] == '.' and not (48 <= ord(s[1]) <= 57):
        print("5")
        return False
    elif s[0] == '-' or s[0] == '+':
        if not (48 <= ord(s[1]) <= 57) and s[1] != '.':
            print("6")
            return False
    decFound, numFound = False, False
    for i in range(len(s)):
        if s[i] != '.' and s[i] != '-' and s[i] != '+' and not (48 <= ord(s[i]) <= 57):
            print("7")
            return False
        if 48 <= ord(s[i]) <= 57:
            numFound = True
        if (s[i] == '+' or s[i] == '-') and i != 0:
            print("8")
            return False
        if s[i] == '.' and decFound == False:
            decFound = True
        elif s[i] == '.' and decFound == True:
            print("9")
            return False
        if s[i] == '.' and i+1 < len(s) and not (48 <= ord(s[i+1]) <= 57):
            print("10")
            return False
    if numFound == False:
        return False
    return True

def isInt(s):
    if len(s) == 0:
        return False
    if len(s) == 1 and not (48 <= ord(s[0]) <= 57):
        return False
    if s[0] != '+' and s[0] != '-' and not (48 <= ord(s[0]) <= 57):
        print("1")
        return False
    for i in range(1,len(s)):
        if not (48 <= ord(s[i]) <= 57):
            print("2")
            return False
    return True