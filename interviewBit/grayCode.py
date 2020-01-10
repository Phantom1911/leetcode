def grayCode(A):
    if A == 1:
        return [0, 1]
    recRes = grayCode(A - 1)
    binRecRes = []
    for number in recRes:
        binRecRes.append(toBinary(number))
    ans = []
    for binary in binRecRes:
        # this fn will return integer
        decimal = toDecimal("0" + binary)
        ans.append(decimal)
    for binary in binRecRes:
        # this fn will return integer
        decimal = toDecimal("1" + binary)
        ans.append(decimal)
    return ans


def toBinary(number):
    if number == 0:
        return "0"
    # number is integer
    binary = ""
    print(type(number),"type of num")
    print(number)
    number = int(number)
    while number > 0:
        binary = binary + str(number % 2)
        number = number // 2
    reversed(binary)
    return binary


def toDecimal(number):
    decimal = 0
    pow = 1
    # print("number is ", number)
    for i in reversed(range(len(number))):
        decimal += int(number[i]) * pow
        pow = pow * 2
    return str(decimal)


if __name__=="__main__":
    print(grayCode(3))