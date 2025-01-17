class Solution:
    def minFallingPathSum(self, matrix) -> int:
        p = matrix[0]
        for r in matrix[1:]:
            for i, e in enumerate(r):
                a, b, c = 101**2, 101**2, 101**2
                if 0 < i:
                    a = p[i - 1]
                if i < len(r) - 1:
                    b = p[i + 1]
                c = p[i]
                r[i] = min(a, b, c) + r[i]
            p = r
        return min(p)
