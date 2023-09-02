class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i, e in enumerate(sorted(t)):
            if i >= len(s) or sorted(s)[i] != e:
                return e
        assert False
        return ""
