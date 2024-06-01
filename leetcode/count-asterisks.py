class Solution:
    def countAsterisks(self, s: str) -> int:
        sz = s.split("|")
        sum_ = 0
        for e in sz[::2]:
            sum_ += e.count("*")
        return sum_
