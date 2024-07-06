from math import gcd
from typing import List


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        x = nums.pop()
        while nums:
            x = gcd(x, nums.pop())
        return x == 1
