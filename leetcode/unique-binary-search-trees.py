class Solution:
    def numTrees(self, n: int) -> int:
        f = lambda x : 1 if x < 2 else x * f(x - 1)
        return f(2 * n)//(f(n) * f(n + 1)) #Catalan numbers
