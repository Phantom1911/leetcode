class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        n = A
        board = [['.' for i in range(n)] for i in range(n)]
        ans = []
        nqueens(0, board, ans)
        return ans

def copyBoard(board):
    res = []
    for row in board:
        tempRow = row[::]
        res.append(tempRow)
    return res

def nqueens(row, board, ans):
    if row == len(board):
        temp = copyBoard(board)
        ans.append(temp)
        # print(ans)
        return
    # row rep the row in which queen is to be placed
    # in the current row, try placing queens from col 0 to n
    n = len(board)
    for col in range(0, n):
        if isSafe(row, col, board):
            board[row][col] = 'Q'
            nqueens(row + 1, board, ans)
            board[row][col] = '.'


def isSafe(row, col, board):
    for i in range(0, row):
        if board[i][col] == 'Q':
            return False
    for i in range(0, col):
        if board[row][i] == 'Q':
            return False
    i, j = row - 1, col - 1
    n = len(board)
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    i,j = row-1 , col+1
    while i<n and j <n:
        if board[i][j] == 'Q':
            return False
        i-=1
        j+=1
    return True

if __name__=="__main__":
    s = Solution()
    print(s.solveNQueens(4))