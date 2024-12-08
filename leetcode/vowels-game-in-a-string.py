class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(e in s for e in "aeiou")
