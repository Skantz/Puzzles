class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        s = 0
        for i in range(1, n + 1):
            if n % i == 0:
                s += 1
            if s == k:
                return i
        return -1
