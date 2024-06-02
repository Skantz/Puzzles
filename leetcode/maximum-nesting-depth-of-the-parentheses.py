class Solution:
    def maxDepth(self, s: str) -> int:
        zum = 0
        maxx = 0
        for e in s:
            if e == "(":
                zum += 1
            if e == ")":
                zum -= 1
            maxx = max(maxx, zum)
        return maxx
