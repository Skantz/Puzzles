from typing import List


class Solution:
    def findRotation(self, m: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(m):
            r = len(m)
            for i in range(r // 2):
                for j in range(i, r - i - 1):
                    t = m[i][j]
                    m[i][j] = m[j][r - i - 1]
                    m[j][r - i - 1] = m[r - i - 1][r - j - 1]
                    m[r - i - 1][r - j - 1] = m[r - j - 1][i]
                    m[r - j - 1][i] = t

        if m == target:
            return True
        for _ in range(3):
            rotate(m)
            if m == target:
                return True
        return False
