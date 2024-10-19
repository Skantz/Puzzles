class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) - 1 < k:
            return s
        def f(x): return sum(int(e) for e in x)
        y = "".join(map(lambda x: str(f(x)), (s[i: i + k] for i in range(0, len(s), k))))
        g = self.digitSum
        return g(y, k)
