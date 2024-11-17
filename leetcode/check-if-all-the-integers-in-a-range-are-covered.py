class Solution:
    def isCovered(self, ranges, left: int, right: int) -> bool:
        return all(any(x <= left <= y for (x, y) in ranges) for left in range(left, right + 1))
