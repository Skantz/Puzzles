class Solution:
    def countCompleteDayPairs(self, hours) -> int:
        return sum(1 for i, e in enumerate(hours) for j, f in enumerate(hours) if i < j and not (i == j or ((e + f) % 24)))
