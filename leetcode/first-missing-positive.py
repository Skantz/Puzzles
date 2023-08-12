class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i, e in enumerate(nums):
            if e <= 0:
                nums[i] = -e + n + 1
        i = 0
        while i < n:
            e = nums[i]
            if nums[i] != i + 1 and e <= n:
                x = nums[e - 1]
                nums[i] = x
                if x <= i and x != e:
                    i -= 1
                nums[e - 1] = e
            i += 1
        for i, e in enumerate(nums):
            if nums[i] != i + 1:
                return i + 1
        return max(nums) + 1
