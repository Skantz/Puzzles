class Solution:
    def getFinalState(self, nums, k: int, multiplier: int):
        n = len(nums)
        from queue import PriorityQueue
        q = PriorityQueue()
        for i, e in enumerate(nums):
            q.put((e, i), e)
        for _ in range(k):
            (x, y) = q.get()
            x *= multiplier
            q.put((x, y), x)
        ret = [0 - 1] * n
        for _ in range(n):
            (x, y) = q.get()
            ret[y] = x
        return ret
