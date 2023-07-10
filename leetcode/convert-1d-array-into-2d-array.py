class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        l = len(original)
        if l != m * n:
            return []
        res = []
        for r in range(m):
            res.append([])
            for c in range(n):
                res[-1].append(original[r * n + c])
        return res
