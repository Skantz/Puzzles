from typing import List


class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        def rotate_(m):
            r = len(m)
            for i in range(r // 2):
                for j in range(i, r - i - 1):
                    t = m[i][j]
                    m[i][j] = m[j][r - i - 1]
                    m[j][r - i - 1] = m[r - i - 1][r - j - 1]
                    m[r - i - 1][r - j - 1] = m[r - j - 1][i]
                    m[r - j - 1][i] = t
        for _ in range(3):
            rotate_(m)
        return m
