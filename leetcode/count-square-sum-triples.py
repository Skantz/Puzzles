class Solution:
    def countTriples(self, n: int) -> int:
        cs = {c**2 for c in range(1, n + 1)}
        return sum(1 if e**2 + f**2 in cs else 0 for e in range(1, n) for f in range(1, n))
