class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        xcount, ocount = 0, 0
        for row in board:
            for i in range(len(row)):
                if row[i] == 'X':
                    xcount += 1
                elif row[i] == 'O':
                    ocount += 1
        if xcount == ocount + 1:
            # if xcount = ocount + 1  it's not possible for o to be in a winning state
            if checkForWin('O', board):
                return False
            return True
        if xcount == ocount:
            # if xcount and ocount are equal it's not possible for x to be in a winning state
            if checkForWin('X', board):
                return False
            return True
        return False


def checkForWin(c, board):
    for i in range(len(board)):
        board[i] = list(board[i])

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] == c:
        return True
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] == c:
        return True
    if board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][1] == c:
        return True
    if board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] == c:
        return True
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[2][0] == c:
        return True
    if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[2][1] == c:
        return True
    if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[2][2] == c:
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] == c:
        return True
    return False