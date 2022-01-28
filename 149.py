def lineThroughPoints(points):
    if len(points) == 1:
        return 1
    lines = set()
    maxCount = 0
    for i in range(len(points) - 1):
        for j in range(i+1, len(points),1):
            p1, p2 = points[i], points[j]
            x1, y1 = p1[0], p1[1]
            x2, y2 = p2[0], p2[1]
            if x1 == x2:
                maxCount = max(pointsOnInfiniteSlopeLine(points, x1),maxCount)
            else:
                sd, sn = getSlope(x1, y1, x2, y2)
                yd, yn = getYIntercept(x1, y1, sd, sn)
                if hashed(sd, sn, yd, yn) not in lines:
                    lines.add(hashed(sd, sn, yd, yn))

    for line in lines:
        sd, sn, yd, yn = unhash(line)
        count = 0
        for point in points:
            if isPointOnLine(sd, sn, yd, yn, point[0], point[1]):
                count += 1
        maxCount = max(maxCount, count)
    return maxCount

def pointsOnInfiniteSlopeLine(points, x):
    count = 0
    for point in points:
        if point[0] == x:
            count+=1
    return count

def unhash(line):
    # print(line)
    arr = list(map(float, line.split(":")))
    return arr[0], arr[1], arr[2], arr[3]


def isPointOnLine(sd, sn, yd, yn, x1, y1):
    lhs = y1 * sn * yn
    rhs = sd * x1 * yn + yd * sn
    return True if lhs == rhs else False


def hashed(a, b, c, d):
    return str(a) + ":" + str(b) + ":" + str(c) + ":" + str(d)


def getSlope(x1, y1, x2, y2):
    sd = y2 - y1
    sn = x2 - x1
    if sn == 0:
        return float("inf") , 1
    neg = isFractionNegative(sd, sn)
    if neg:
        sd_temp, sn_temp = reduce(abs(sd), abs(sn))
        if sd_temp == 0:
            return 0, 1
        sd, sn = -sd_temp, sn_temp
    else:
        sd, sn = reduce(sd, sn)
        if sd == 0:
            return 0, 1
    return sd, sn


def isFractionNegative(a, b):
    return True if (a > 0 and b < 0) or (a < 0 and b > 0) else False


def getYIntercept(x1, y1, sd, sn):
    if sd == 0:
        return y1 , 1
    if sd == float("inf"):
        return float("inf") , 1
    yd = (sn * y1) - (x1 * sd)
    yn = sn
    yd, yn = reduce(yd, yn)
    return yd, yn


def reduce(den, num):
    gcd = getgcd(den, num)
    # print(f"{den} , {num} , {gcd}")
    return den / gcd, num / gcd


def getgcd(a, b):
    while True:
        if a == 0:
            return b
        if b == 0:
            return a
        a, b = b, a % b

if __name__=="__main__":
    print(lineThroughPoints([
    [1, 1],
    [1, 2],
    [1, 3],
    [1, 4],
    [1, 5],
    [2, 1],
    [2, 2],
    [2, 3],
    [2, 4],
    [2, 5],
    [3, 1],
    [3, 2],
    [3, 4],
    [3, 5],
    [4, 1],
    [4, 2],
    [4, 3],
    [4, 4],
    [4, 5],
    [5, 1],
    [5, 2],
    [5, 3],
    [5, 4],
    [5, 5],
    [6, 6],
    [2, 6]
  ]))