from typing import List


class Solution:

    def comp(self, ival_x: List[int], ival_y: List[int]):
        assert len(ival_x) == 2
        assert len(ival_y) == 2
        b1 = ival_y[0] <= ival_x[1] <= ival_y[1]
        b2 = ival_x[0] <= ival_y[1] <= ival_x[1]
        return b1 or b2

    def merge(self, ival_x: List[int], ival_y: List[int]):
        assert self.comp(ival_x, ival_y)
        return [min(ival_x[0], ival_y[0]), max(ival_x[1], ival_y[1])]

    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        if len(intervals) < 1:
            return [newInterval]
        comp = self.comp
        if not any(comp(x, newInterval) for x in intervals):
            return sorted(intervals + [newInterval])
        r = next((x for x in intervals if comp(x, newInterval)))
        i = intervals.index(r)
        m = self.merge(r, newInterval)
        return self.insert(intervals[:i] + intervals[i + 1:], m)
