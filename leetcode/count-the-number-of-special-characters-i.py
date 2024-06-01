class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        return len({w for w in word if w.lower() in word and w.upper() in word})//2
