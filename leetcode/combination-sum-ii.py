from collections import Counter
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        c = Counter(candidates)
        candidates = []
        for e in c:
            candidates += [e] * min(30, target//e + target % e, c[e])
        x = self.combination_sum(candidates, target)
        if x == [[]]:
            return []
        return [list(e) for e in {tuple(sorted(e)) for e in x}]

    def combination_sum(self, candidates, target):
        if target < 0:
            return None
        if target == 0:
            return [[]]
        if sum(candidates) < target:
            return [[]]
        if sum(candidates) == target:
            return [candidates]
        rets = []
        seen = set()
        for i, c in enumerate(candidates):
            x, y = tuple(candidates[:i] + candidates[i + 1:]), target - c
            if (x, y) in seen:
                continue
            seen.add((x, y))
            e = self.combination_sum(candidates[:i] + candidates[i + 1:], target - c)
            if e:
                rets += [[c] + e_ for e_ in e]
        return rets
