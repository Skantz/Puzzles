from typing import List


class NaiveSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [2, 7, 11, 15]
        # t : 9
        # -> [0,1]
        for (i, n) in enumerate(nums):
            for (j, m) in enumerate(nums):
                if ((i != j) and (n + m == target)):
                    return [i + 1, j + 1]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inverse_and_index = {}
        for (i, n) in enumerate(nums):
            # 0 2    1 7      2 11     3 15
            inverse_and_index[n] = i
        for (i, n) in enumerate(nums):
            try:
                idx = inverse_and_index[target - n]
                if idx != i:
                    return [i + 1, idx + 1]
            except KeyError:
                continue
