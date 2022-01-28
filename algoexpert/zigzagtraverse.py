def zigzagTraverse(array):
    # realize that at any point of time you are either going up or down
    # the movement to the right happens when you are trying to go up or down and can't
    # the movement to the down happens when you can't go up/down or right
    a, b = 0, 0
    m, n = len(array), len(array[0])
    goingDown = True
    ans = []
    traversed = 0
    while len(ans) != m*n:
        ans.append(array[a][b])
        if goingDown:
            # try to go diagonally down
            c, d = a + 1, b - 1
            e, f = a + 1, b
            g, h = a , b+1
            if isinbounds(c, d, m, n):
                a, b = c, d
                traversed += 1
            elif isinbounds(e, f, m, n):
                a, b = e, f
                traversed += 1
                goingDown = False
            elif isinbounds(g, h, m, n):
                a, b = g, h
                traversed += 1
                goingDown = False
        else:
            c, d = a - 1, b + 1
            e, f = a, b + 1
            g, h = a + 1, b
            if isinbounds(c, d, m, n):
                a, b = c, d
                traversed += 1
            elif isinbounds(e, f, m, n):
                a, b = e, f
                traversed += 1
                goingDown = True
            elif isinbounds(g, h, m, n):
                a, b = g, h
                goingDown = True
                traversed += 1
    return ans


def isinbounds(x, y, m, n):
    return 0 <= x < m and 0 <= y < n

if __name__ =="__main__":
    print(zigzagTraverse([
  [1, 3, 4, 10],
  [2, 5, 9, 11],
  [6, 8, 12, 15],
  [7, 13, 14, 16]
]))
    '''
    if you were going diag down and come to the 0th col => go down
    if you were going diag down and come to the m-1th row => go right
    if you were going diag up and come to the n-1th col => go down
    if you were going diag up and come to the 0th row => go right

    '''
