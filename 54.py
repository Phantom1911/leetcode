def safe(a, b, m, n, seen):
    return True if 0 <= a < m and 0 <= b < n and str(a) + ":" + str(b) not in seen else False


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # the order of directions is always right,down,left,up
        # dir is changed when we go out ouf bound or encounter already visited element
        m, n = len(matrix), len(matrix[0])
        currdir = 'right'
        seen = set()
        ans = []
        i, j = 0, 0
        while len(seen) != m * n:
            if safe(i, j, m, n, seen):
                ans.append(matrix[i][j])
                seen.add(str(i) + ":" + str(j))
                if currdir == 'right':
                    i, j = i, j + 1
                elif currdir == 'left':
                    i, j = i, j - 1
                elif currdir == 'up':
                    i, j = i - 1, j
                elif currdir == 'down':
                    i, j = i + 1, j
            elif currdir == 'right':
                i, j = i + 1, j - 1
                currdir = 'down'
            elif currdir == 'down':
                i, j = i - 1, j - 1
                currdir = 'left'
            elif currdir == 'left':
                i, j = i - 1, j + 1
                currdir = 'up'
            elif currdir == 'up':
                i, j = i + 1, j + 1
                currdir = 'right'

        return ans