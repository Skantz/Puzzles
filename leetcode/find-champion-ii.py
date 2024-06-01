from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if not edges and n < 2:
            return 0
        seen = set(range(n))
        not_these = set()
        for e in edges:
            not_these.add(e[1])
        maybe = seen - not_these
        if len(maybe) != 1:
            return -1
        return list(maybe)[0]
