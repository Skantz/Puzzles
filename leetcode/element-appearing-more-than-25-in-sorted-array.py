class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        s = set(arr)
        return next(c for c in s if arr.count(c) / len(arr) > 0.25)
