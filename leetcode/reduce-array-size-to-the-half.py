class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter
        l = sorted(list(Counter(arr).values()))[::-1]
        s, c = 0, 0
        while s < len((arr))/2:
            s += l[c]
            c += 1
        return c
