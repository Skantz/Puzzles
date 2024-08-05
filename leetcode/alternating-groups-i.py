from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        s = 0
        n = len(colors)
        for j in range(0, len(colors)):
            i = (j - 1) % n
            k = (j + 1) % n
            if colors[j] not in [colors[i], colors[k]]:
                s += 1
        return s
