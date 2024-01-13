import bisect
from typing import List


class Solution:

    def bin_search(self, lst, x):
        i = bisect.bisect_left(lst, x)
        if i == len(lst) or lst[i] != x:
            return -1
        return i

    def search(self, nums: List[int], target: int) -> int:
        bins = [False] + [nums[i] < nums[0] for i in range(1, len(nums))]
        idx = max(0, self.bin_search(bins, True))  # no rot -> ret -1 -> 0-rot
        f1 = self.bin_search(nums[:idx], target)
        f2 = self.bin_search(nums[idx:], target)
        return f1 if f2 == -1 else f2 + idx
