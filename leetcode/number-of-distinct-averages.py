class Solution:
    def distinctAverages(self, nums) -> int:
        n = len(nums)
        i = 0
        j = n - 1
        nums.sort()
        rets = set()
        while i <= j:
            if i == j:
                rets.add(nums[i])
                break
            x = nums[i]
            y = nums[j]
            rets.add((x + y) / 2)
            i += 1
            j -= 1
        return len(rets)
