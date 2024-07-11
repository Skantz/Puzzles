from typing import List
from collections import Counter


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        c = Counter(nums)
        nums = []
        for e in c:
            if c[e] > 4:
                nums += [e] * 4
            else:
                nums += [e] * c[e]
        two = {}
        for i, e in enumerate(nums):
            for j, f in enumerate(nums):
                if j - 1 < i:
                    continue
                if e + f in two:
                    two[e + f].append((i, j))
                else:
                    two[e + f] = [(i, j)]
        ret = set()
        for k1 in two:
            for k2 in two:
                if k1 + k2 != target:
                    continue
                assert k1 + k2 == target
                for (x, y) in two[k1]:
                    for (x_, y_) in two[k2]:
                        if len(set([x, y, x_, y_])) < 4:
                            continue
                        ret.add((nums[x], nums[y], nums[x_], nums[y_]))
        return [list(e) for e in list({tuple(sorted(list(e))) for e in ret})]
