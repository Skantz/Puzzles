class Solution:
    def countOrders(self, n: int) -> int:
        def f(x): return 1 if x < 2 else x * f(x - 1)
        return f(2 * n)//2**n % (10**9 + 7)
