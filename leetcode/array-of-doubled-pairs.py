from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        if not arr:
            return True
        a = [-e for e in arr if e < 0]
        b = [e for e in arr if e >= 0]
        if len(a) > 0:
            return self.canReorderDoubled(a) and self.canReorderDoubled(b)
        arr.sort()
        while arr:
            try:
                i = arr.index(2 * arr[0])
            except ValueError:
                return False
            arr = (arr[1:i] + arr[i + 1:])
        return True
