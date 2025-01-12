class Solution:
    def numRescueBoats(self, xs, k: int) -> int:
        r = 0
        xs.sort()
        i = 0
        j = len(xs) - 1
        while i < j:
            if xs[i] + xs[j] <= k:
                i += 1
            j -= 1
            r += 1
        return r + (1 if i == j else 0)
