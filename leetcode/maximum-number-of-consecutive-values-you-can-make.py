from typing import List


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        if not coins:
            return 1
        coins.sort()
        if 1 < coins[0]:
            return 1
        s = 1
        for c in coins:
            if c > s:
                break
            s += c
        return s
