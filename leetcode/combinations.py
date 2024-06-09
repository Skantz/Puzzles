from typing import List
from functools import cache


class Solution:
    @cache
    def combine(self, n: int, k: int, c=1) -> List[List[int]]:
        if n < 1:
            return [[]]
        if k < 1:
            return [[]]
        if n == k:
            return [[e for e in list(range(c, n + 1))]]
        combine = self.combine
        rets = []
        for i in range(c, n + 1):
            rets += [[i] + e for e in combine(n, k - 1, c + 1)]
        rets.sort()
        no_dupe = lambda list_of_list: [list(e) for e in list({tuple(sorted(e)) for e in list_of_list})]
        no_dub = lambda list_of_list: [list(e) for e in list({tuple(sorted(e)) for e in list_of_list}) if sorted(list(e)) == sorted(list(set(e)))]
        return sorted(no_dub(no_dupe(rets)))
