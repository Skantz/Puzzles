class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        dct = {i:[] for i in range(24)}
        for c in candidates:
            b = bin(c)[2:][::-1]
            for i, e in enumerate(b):
                if e == "1":
                    dct[i].append(c)
        return max(len(e) for e in dct.values())
