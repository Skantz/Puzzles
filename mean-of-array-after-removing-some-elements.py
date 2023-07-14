class Solution:
    def trimMean(self, arr: List[int]) -> float:
        return (lambda n: sum(sorted(arr)[n//20: (n * 19)//20])/(0.9 * n))(len(arr))
