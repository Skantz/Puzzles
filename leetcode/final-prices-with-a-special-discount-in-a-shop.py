class Solution:
    def finalPrices(self, prices):
        def f(x, i): return next((e for e in prices[i + 1:] if e <= x))
        def g(x, i):
            try:
                return f(x, i)
            except StopIteration:
                return 0
        return [x - g(x, i) for i, x in enumerate(prices)]
