class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        a, b = s[:n // 2], s[n // 2:]
        print(a, b)
        lst = ["a", "e", "i", "o", "u"]
        return len([e for e in a if e.lower() in lst]) == len([e for e in b if e.lower() in lst])
