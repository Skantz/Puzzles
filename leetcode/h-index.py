class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) <= 1:
            return min(1, citations[0])
        maxx = 0
        for i, e in enumerate(sorted(citations)[::-1]):
            maxx = max(maxx, min(i + 1, e))
        return maxx
