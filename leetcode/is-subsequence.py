class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = "".join(e for e in t if e in s)
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            x = s[i]
            y = t[j]
            j = j + 1
            i = i + (1 if x == y else 0)
        return len(s) - 1 < i
