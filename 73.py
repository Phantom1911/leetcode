class Solution:
    def hashed(self, i, j):
        return str(i) + ":" + str(j)

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        origzeros = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    origzeros.add(self.hashed(i, j))

        n = len(matrix)
        m = len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0 and self.hashed(i, j) in origzeros:
                    k = j + 1
                    while k < m:
                        matrix[i][k] = 0
                        k += 1
                    k = j - 1
                    while k >= 0:
                        matrix[i][k] = 0
                        k -= 1
                    k = i + 1
                    while k < n:
                        matrix[k][j] = 0
                        k += 1
                    k = i - 1
                    while k >= 0:
                        matrix[k][j] = 0
                        k -= 1

