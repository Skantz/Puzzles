class Solution:
    def scoreOfString(self, s: str) -> int:
        sz = 0
        for i in range(1, len(s)):
            sz += abs(ord(s[i]) - ord(s[i - 1]))
        return sz
