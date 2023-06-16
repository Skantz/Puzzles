class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if timeSeries == []:
            return 0
        n1 = timeSeries[0]
        s = 0
        for i in range(1, len(timeSeries)):
            n2 = timeSeries[i]
            s += min(duration, n2 - n1)
            n1 = n2
        return s + duration
