class Solution:
    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, board):

        empty = [-1, -1]
        # When no empty positions left then we have our complete sudoku
        if not self.find_empty_location(board, empty):
            return True

        r, c = empty[0], empty[1]

        for num in range(1, 10):
            # chekc if our choice of placing num at certain r,c is valid or not
            if self.isvalid(num, r, c, board):
                board[r][c] = str(num)

                if self.solveSudoku(board):
                    return True
                # if the taken choice did not yield any solution then backtrack
                board[r][c] = '.'

    # function to find empty cell in board
    def find_empty_location(self, board, empty):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty[0] = i
                    empty[1] = j
                    return True
        return False

    # function to check if we can successfully place a number on a particular cell
    def isvalid(self, num, r, c, board):
        # checking if num exists in the corresponding column
        for i in range(9):
            if board[i][c] == str(num):
                return False
        # checking if num exists in the coresponding row
        for j in range(9):
            if board[r][j] == str(num):
                return False
        # checking if the number exists in that particular 3X3 block of sudoku
        r = r - r % 3
        c = c - c % 3
        for i in range(3):
            for j in range(3):
                if board[i + r][j + c] == str(num):
                    return False
        return True

