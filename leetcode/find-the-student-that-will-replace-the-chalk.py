from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        m = k % s
        i = 0
        c = 0
        while c < m:
            c += chalk[i]
            if not c <= m:
                break
            i += 1
        return i
