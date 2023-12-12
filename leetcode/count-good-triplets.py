class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        s = 0
        l = arr
        n = len(l)
        for i in range(n):
            for j in range(i + 1, n):
                for k  in range(j + 1, n):
                    if abs(l[i] - l[j]) <= a\
                    and abs(l[j] - l[k]) <= b\
                    and abs(l[i] - l[k]) <= c:
                        s += 1
        return s
