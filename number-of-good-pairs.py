class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    ans += 1
        return ans
    def numIdenticalPairs_(self, nums: List[int]) -> int:
        # Slower
        from collections import Counter
        c = Counter(nums)
        s = 0
        for e in c:
            if c[e] > 1:
                s += (c[e] * (c[e] - 1))//2
        return s
