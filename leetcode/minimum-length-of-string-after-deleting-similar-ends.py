class Solution:
    def minimumLength(self, s: str) -> int:
        while s and s[0] == s[-1]:
            if not s.lstrip(s[0]):
                if 1 < len(set(s)):
                    break
                if 1 < len(s):
                    return 0
                return 1
            s = s.lstrip(s[0])
            s = s.rstrip(s[-1])
        return len(s)
