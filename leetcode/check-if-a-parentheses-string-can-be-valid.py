class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2:
            return False
        c1, c2 = 0, 0
        for i in range(n):
            if int(locked[i]) and s[i] == ')':
                c1 = c1 - 1
            else:
                c1 += 1
            if int(locked[n - i - 1]) and s[n - i - 1] == '(':
                c2 = c2 - 1
            else:
                c2 += 1
            if c1 < 0 or c2 < 0:
                return False
        return True
