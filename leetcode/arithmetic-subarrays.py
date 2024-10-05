from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        rets = []
        for i, j in zip(l, r):
            if j - i < 2:
                rets.append(True)
                continue
            lst = nums[i:j + 1]
            lst.sort()
            d = lst[1] - lst[0]
            rets.append(all(lst[i + 1] - lst[i] == d for i in range(len(lst) - 1)))
        return rets
