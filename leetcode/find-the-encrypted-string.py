class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        return (lambda k: s[k:] + s[:k])(k % len(s))
