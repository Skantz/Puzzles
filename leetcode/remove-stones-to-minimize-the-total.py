class Solution:
    def minStoneSum(self, piles, k: int) -> int:
        from queue import PriorityQueue
        q = PriorityQueue()
        for i, e in enumerate(piles):
            q.put((-e, i))
        for _ in range(k):
            e, i = q.get()
            q.put(((e - (int(e / 2)), i)))
        s = 0
        while not q.empty():
            e, i = q.get()
            s -= e
        return s
