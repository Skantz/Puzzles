class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxrow = 0
        s = 0
        i = 0
        for r in mat:
            ss = r.count(1)
            if ss > s:
                s = ss
                maxrow = i
            i += 1
        return [maxrow, s]
