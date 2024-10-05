class Solution:
    def shuffle(self, nums, n: int):
        return [nums[i + j * n] for i in range(n) for j in range(2)]
