class Solution:
    def countPoints(self, rings: str) -> int:
        pairs = list(set([(rings[2*i + 1], rings[2*i]) for i in range(len(rings)//2)]))
        return len([e for e in pairs if [e_[0] for e_ in pairs].count(e[0]) == 3])//3
