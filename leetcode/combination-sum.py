from typing import List


def no_dupe(list_of_list):
    return [list(e) for e in {tuple(sorted(e)) for e in list_of_list}]

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target < 0:
            return None
        if target == 0:
            return [[]]
        rets = []
        for c in candidates:
            e = self.combinationSum(candidates, target - c)
            if e:
                rets += [[c] + e_ for e_ in e]
        return no_dupe(rets)
