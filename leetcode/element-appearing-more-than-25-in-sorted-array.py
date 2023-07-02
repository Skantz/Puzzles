class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return next(c for c in set(arr) if arr.count(c) > len(arr) * 0.25)
