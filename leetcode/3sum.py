from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dct = {}
        for i, e in enumerate(nums):
            if e in dct and len(dct[e]) < 3:
                dct[e] += [i]
            elif e not in dct:
                dct[e] = [i]
        trips = set()
        for i, e1 in enumerate(nums):
            for j, e2 in enumerate(nums):
                if j <= i:
                    continue
                s = e1 + e2
                if -s in dct and not all(e in [i, j] for e in dct[-s]):
                    trips.add(tuple(sorted([e1, e2, -s])))
        return list(trips)


"""
nums = [1, 1, 2, ..]
dct  = [] -> [1 : [0]]
    -> [1 : [0, 1]]
    -> [1 : [0, 1], 2 : [2]] -> ..

trips = {}

[#, 1, 2, ..]
[#, #, 2, ..]
[#, #, #, ..]
[#, .. .. # ]

i = 0, j = 1
-> tup := (1, 2)
-> sum(tup) = 3
-> -s = -3


"""
