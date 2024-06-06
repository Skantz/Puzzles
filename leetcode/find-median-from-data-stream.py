from bisect import insort_left


class MedianFinder:

    def __init__(self):
        self.s = []

    def addNum(self, x: int) -> None:
        insort_left(self.s, x)

    def findMedian(self) -> float:
        n = len(self.s)
        if not n:
            return 0
        if not n % 2:
            return self.s[n // 2 - 1] / 2 + self.s[n // 2 + 1 - 1] / 2
        else:
            return self.s[n // 2]
