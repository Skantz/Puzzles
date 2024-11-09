class Solution:
    def averageValue(self, xs) -> int:
        ys = [x for x in xs if not x % 6]
        return sum(ys) // len(ys) if len(ys) else 0
