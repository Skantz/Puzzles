class Solution:
    def firstUniqChar(self, s: str) -> int:
        try:
            return s.index(next(filter(lambda x: s.count(x) == 1, s)))
        except StopIteration:
            return -1
