class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = list(range(n))
        goal = list(perm)
        def do(perm): return [perm[i // 2] if i % 2 == 0 else perm[n // 2 + (i - 1) // 2] for i in range(n)]
        perm = do(perm)
        s = 1
        while perm != goal:
            perm = do(perm)
            s += 1
        return s
