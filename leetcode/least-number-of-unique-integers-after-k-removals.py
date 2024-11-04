class Solution:
    def findLeastNumOfUniqueInts(self, arr, k: int) -> int:
        from collections import Counter
        cs = list(Counter(arr).values())
        ret = len(set(arr))
        cs.sort()
        for e in cs:
            k -= e
            if k < 0:
                break
            ret -= 1
        return ret
