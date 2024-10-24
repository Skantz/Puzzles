class Solution:
    def maximumProduct(self, nums, k: int) -> int:
        from queue import PriorityQueue
        q = PriorityQueue()
        for e in nums:
            q.put(e)
        for _ in range(k):
            q.put(q.get() + 1)
        y = 1
        while not q.empty():
            y = y * q.get() % (10 ** 9 + 7)
        return y
