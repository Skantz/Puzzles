from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        c = {}
        for row in matrix:
            for e in [tuple(row), tuple([0 if e == 1 else 1 for e in row])]:
                if e in c:
                    c[e] += 1
                else:
                    c[e] = 1
        return max(c.values())
