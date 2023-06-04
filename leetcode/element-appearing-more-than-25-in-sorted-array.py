class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        s, n = set(arr), len(arr)
        lim = n * 0.25
        return next(c for c in s if arr.count(c) > lim)
