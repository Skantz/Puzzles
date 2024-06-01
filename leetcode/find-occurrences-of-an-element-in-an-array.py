from typing import List


class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        lookup = []
        queries = [e - 1 for e in queries]
        for i, e in enumerate(nums):
            if e == x:
                lookup.append(i)
        rets = []
        for e in queries:
            try:
                rets.append(lookup[e])
            except IndexError:
                rets.append(-1)
        return rets
