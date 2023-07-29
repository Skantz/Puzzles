class NaiveSolution:
    from random import randint
    def __init__(self, nums: List[int]):
        self.nums=nums

    def pick(self, target: int) -> int:
        n = self.nums.count(target)
        m = randint(0, n - 1)
        c = 0
        return [i for i, n in enumerate(self.nums) if (n == target)][m]
class Solution:
    from random import randint
    def __init__(self, nums: List[int]):
        self.nums=nums
        self.idxs = {}
        for i, e in enumerate(nums):
            try:
                self.idxs[e].append(i)
            except KeyError:
                self.idxs[e] = [i]

    def pick(self, target: int) -> int:
        n = len(self.idxs[target])
        m = randint(0, n - 1)
        c = 0
        return self.idxs[target][m]
