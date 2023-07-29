class Solution:
    from random import randint
    def __init__(self, nums: List[int]):
        self.nums=nums

    def pick(self, target: int) -> int:
        n = self.nums.count(target)
        m = randint(0, n - 1)
        c = 0
        return [i for i, n in enumerate(self.nums) if (n == target)][m]
