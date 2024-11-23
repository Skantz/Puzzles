class Solution:
    def numSpecial(self, mat) -> int:
        c = 0
        def col(j): return [mat[i][j] for i in range(len(mat))]
        for i, e in enumerate(mat):
            if not e.count(1) == 1:
                continue
            for j, g in enumerate(e):
                if g == 1 and col(j).count(1) == 1:
                    c += 1
        return c
