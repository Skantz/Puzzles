from random import randint


class NaiveSolution:
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target: int) -> int:
        n = self.nums.count(target)
        m = randint(0, n - 1)
        return [i for i, n in enumerate(self.nums) if n == target][m]


class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.idxs = {}
        for i, e in enumerate(nums):
            try:
                self.idxs[e].append(i)
            except KeyError:
                self.idxs[e] = [i]

    def pick(self, target: int) -> int:
        n = len(self.idxs[target])
        m = randint(0, n - 1)
        return self.idxs[target][m]
