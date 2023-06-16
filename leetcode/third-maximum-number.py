class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        l = sorted(list(s))
        if len(l) < 3:
            return l[-1]
        return l [-3]
