class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        rets = []
        for i in range(1, n - 1):
            if mountain[i - 1] < mountain[i]\
           and mountain[i + 1] < mountain[i]:
                rets.append(i)
        return rets
