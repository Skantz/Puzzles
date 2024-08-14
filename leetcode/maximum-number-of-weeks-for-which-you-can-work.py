class Solution:
    def numberOfWeeks(self, xs) -> int:
        x = max(xs)
        s = sum(xs) - x
        return min(sum(xs), 1 + s * 2)
