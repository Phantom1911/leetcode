def reverseString(s):
    if len(s) == 1:
        return s
    return reverseString(s[1:])+s[0]

if __name__ == "__main__":
    print(reverseString("aastik"))