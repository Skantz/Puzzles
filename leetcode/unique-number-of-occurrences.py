class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mapp = {}
        for v in set(arr):
            mapp[v] = 0
        for v in arr:
            mapp[v] += 1
        return sorted(list(mapp.values())) == sorted(list(set(mapp.values()))) 
