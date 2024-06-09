from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        i = 0
        skip = 0
        skip_set = set()
        while i + skip < n - 1:
            do_merge = intervals[i + 1 + skip][0] - 1 < intervals[i][1] #<=
            if do_merge:
                intervals[i][1] = max(intervals[i][1], intervals[i + 1 + skip][1])
                skip_set.add(i + 1 + skip)
                skip = skip + 1
            else:
                i += 1
                skip = 0
        intervals = [(x, y) for i, (x, y) in enumerate(intervals) if i not in skip_set]
        return intervals
