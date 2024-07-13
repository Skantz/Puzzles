from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

    def findKthLargest_(self, nums: List[int], k: int) -> int:
        from queue import PriorityQueue
        q = PriorityQueue()
        for n in nums:
            q.put(-n)
        for _ in range(k):
            e = q.get()
        return -e
