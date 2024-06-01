from typing import List


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        mems = {}
        def is_prime(n):
            if n in mems:
                return mems[n]
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    mems[n] = False
                    return False
            mems[n] = True
            return True
        indices = []
        for i, e in enumerate(nums):
            if is_prime(e):
                indices.append(i)
        return max(indices) - min(indices)
