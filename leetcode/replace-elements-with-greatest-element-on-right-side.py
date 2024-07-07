from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        run_max = []
        maxx = -1
        for e in arr[::-1]:
            run_max.append(maxx)
            maxx = max(maxx, e)
        run_max = run_max[::-1]
        for i, e in enumerate(run_max):
            arr[i] = e
        return arr
