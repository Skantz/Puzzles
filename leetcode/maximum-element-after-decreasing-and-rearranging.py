from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        if len(arr) < 1:
            assert False; return -1
        if len(arr) < 2:
            return 1
        arr.sort()
        arr[0] = 1
        while 1 < len(arr):
            x, y = arr[0], arr[1]
            # assert x <= y
            if 1 < y - x:
                arr[1] = x + 1
            arr.pop(0)
        return arr[-1]
