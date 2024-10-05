from typing import List


class Solution:
    def kthSmallest(self, m: List[List[int]], k: int) -> int:
        k -= 1

        def flatten(x):
            if not x:
                return []
            return(x[0] + flatten(x[1:]))
        v = flatten(m)
        v.sort()
        return v[k]
