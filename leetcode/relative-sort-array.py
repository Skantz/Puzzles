from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ret = []
        for e in arr2:
            ret += [e] * arr1.count(e) if e in arr1 else []
        return ret + sorted([e for e in arr1 if e not in ret])
