class Solution:
    def minSwaps(self, s: str) -> int:
        c_0, c_1, n = s.count("0"), s.count("1"), len(s)
        x = len([i for i in range(n//2 + 1 if n % 2 else 0) if s[2*i] == "0"])
        y = len([i for i in range(n//2 + 1 if n % 2 else 0) if s[2*i] == "1"])
        return -1 if abs(c_0 - c_1) > 0\
            else min(x, y) if c_0 == c_1 else x if c_0 < c_1 else y
