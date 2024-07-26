from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        xs = [x for x in nums if not x % 2]
        ys = [y for y in nums if y % 2]
        return [e for f in zip(xs, ys) for e in f]
