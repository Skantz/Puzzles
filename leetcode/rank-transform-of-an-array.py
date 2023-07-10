class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rs, i = {}, 1
        for e in sorted(list(set(arr))):
            rs[e], i = i, i + 1
        return [rs[e] for e in arr]
