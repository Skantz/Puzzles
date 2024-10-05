class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(j)**2 for j in list(str(n)))
        return True if n == 1 else False
