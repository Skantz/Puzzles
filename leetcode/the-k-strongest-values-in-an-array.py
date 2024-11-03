class Solution:
    def getStrongest(self, arr, k: int):
        arr = sorted(arr)
        m = arr[(len(arr) - 1) // 2]
        def f(x): return (0 - abs(x - m), 0 - x)
        return sorted(arr, key=f)[:k]
