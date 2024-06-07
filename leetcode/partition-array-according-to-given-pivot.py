from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        x = [e for e in nums if e < pivot]
        y = [e for e in nums if pivot < e]
        return x + [pivot] * nums.count(pivot) + y
