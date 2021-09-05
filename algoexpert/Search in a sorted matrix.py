class Solution:
    def searchMatrix(self, matrix, target):
        currRow, currCol = 0, 0
        m = len(matrix)
        n = len(matrix[0])
        while currRow < m and currCol < n:
            if (matrix[currRow][currCol] == target):
                return True
            if matrix[currRow][n - 1] < target:
                currRow += 1
            if matrix[m - 1][currCol] < target:
                currCol += 1

        return False


if __name__=="__main__":
    print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))