class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        return len([i for i in list(range(1, max(a, b) + 1)) if not (a%i or b%i)])
