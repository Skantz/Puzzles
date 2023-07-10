class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for e in [str(i)*3 for i in range(9, -1, -1)]:
            if e in num:
                return e
        return ""
