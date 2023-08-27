def no_dupe(list_of_list):
    return [list(e) for e in list(set([tuple(sorted(e)) for e in list_of_list]))]

class Solution:
    def partition(self, n, j):
        yield (n,)
        for i in range(j, n//2 + 1):
            for p in self.partition(n-i, i):
                yield (i,) + p
    # Solution 1
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        rets = []
        for p in self.partition(target, 1):
            if set(p).issubset(set(candidates)):
                rets.append(list(p))
        return rets
    # Solution 2
    def combinationSum_(self, candidates: List[int], target: int) -> List[List[int]]:
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
