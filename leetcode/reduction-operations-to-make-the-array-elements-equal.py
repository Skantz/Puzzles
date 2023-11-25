class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(set(nums))
        if n < 2:
            return 0
        nums.sort()
        s, c = 0, 0
        prev = nums[0]
        for i, e in enumerate(nums):
            if i == 0:
                continue
            if e != prev:
                prev = e
                c += 1
            s += c
        return s
