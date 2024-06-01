from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        x, y = edges[0][0], edges[0][1]
        for e in edges[1:]:
            if x in e:
                return x
            if y in e:
                return y
        assert False
