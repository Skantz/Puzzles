class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [-i for i in range(1, n//2 + 1)] + ([0] if n % 2 else []) + list(range(1, n//2 + 1))
