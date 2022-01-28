def boggleBoard(board, words):
    ans = []
    m, n = len(board), len(board[0])
    for w in ((words)):
        flag = False
        # check for each cell of the board
        for i in range(m):
            for j in range(n):
                if board[i][j] != w[0]:
                    continue
                seen = set()
                flag = flag or dfs(board, seen, i, j, "", w)
                if flag:
                    ans.append(w)
                    break
            if flag:
                break
    return ans


def dfs(board, seen, i, j, currstr, w):
    currstr += board[i][j]
    seen.add(hashed(i, j))
    if len(currstr) > len(w):
        return False
    if currstr == w:
        return True
    dirs = [[-1, 0], [1, 1], [0, 1], [0, -1], [1, 0], [-1, 1], [-1, -1], [1, -1]]
    ans = False
    m, n = len(board), len(board[0])
    for dire in dirs:
        newI, newJ = i + dire[0], j + dire[1]
        if inbounds(newI, newJ, m, n) and hashed(newI, newJ) not in seen and currstr + board[newI][newJ] == w[
                                                                                                            :len(currstr) + 1]:
            ans = ans or dfs(board, seen, newI, newJ, currstr, w)
            if ans:
                return True
    return ans


def hashed(i, j):
    return str(i) + ":" + str(j)


def inbounds(a, b, m, n):
    if 0 <= a < m and 0 <= b < n:
        return True
    return False

if __name__=="__main__":
    print(boggleBoard([
    ["c", "o", "m"],
    ["r", "p", "l"],
    ["c", "i", "t"],
    ["o", "a", "e"],
    ["f", "o", "d"],
    ["z", "r", "b"],
    ["g", "i", "a"],
    ["o", "a", "g"],
    ["f", "s", "z"],
    ["t", "e", "i"],
    ["t", "w", "d"]
  ],
   ["commerce", "complicated", "twisted", "zigzag", "comma", "foobar", "baz", "there"]))