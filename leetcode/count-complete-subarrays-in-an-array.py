class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        allzet = set(nums)
        n = len(nums)
        m = len(allzet)
        s = 0
        for i in range(n - m + 1): # # elements >= m
            runzet = set()
            j = 0
            while runzet != allzet and i + j < n: # set() =? set() => O(n)
                runzet.add(nums[i + j])
                j += 1
            if runzet == allzet:
                s += (n - i - j + 1) # [5, 5, 5, 5], i = 0 => add 4
        return s
