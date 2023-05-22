class Solution:
    def partition(self, n, j):
        yield (n,)
        for i in range(j, n//2 + 1):
            for p in self.partition(n-i, i):
                yield (i,) + p
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        rets = []
        for p in self.partition(target, 1):
            if set(p).issubset(set(candidates)):
                rets.append(list(p))
        return rets
