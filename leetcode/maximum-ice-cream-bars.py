from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i = 0
        while i < len(costs) and 0 < coins:
            coins -= costs[i]
            i += 1
        return i - (1 if coins < 0 else 0)
