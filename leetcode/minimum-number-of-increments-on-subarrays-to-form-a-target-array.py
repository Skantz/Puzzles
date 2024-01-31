from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        s = target[0]
        for i in range(1, n):
            s += max(0, target[i] - target[i - 1])
        return s
