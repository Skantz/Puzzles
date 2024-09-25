class Solution:
    def halveArray(self, nums) -> int:
        s = sum(nums)
        from queue import PriorityQueue
        q = PriorityQueue()
        for e in nums:
            q.put((0 - 1) * e)
        c = 0
        sum_ = sum(nums) / 2
        while s > sum_:
            e = q.get()
            s += e / 2
            q.put(e / 2)
            c += 1
        return c
