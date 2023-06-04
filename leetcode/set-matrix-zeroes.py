class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        zeros_tup = [(i, j) for i in range(n) for j in range(m) if matrix[i][j] == 0]
        for tup in zeros_tup:
            i = tup[0]
            j = tup[1]
            for k in range(m):
                matrix[i][k] = 0
            for k in range(n):
                matrix[k][j] = 0
