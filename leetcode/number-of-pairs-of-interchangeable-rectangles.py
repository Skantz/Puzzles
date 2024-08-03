from typing import List


class Solution:
    def interchangeableRectangles(self, xs: List[List[int]]) -> int:
        from collections import Counter; c = Counter([x[0]/x[1] for x in xs])
        return sum(c[e] * (c[e] - 1)//2 for e in c)
