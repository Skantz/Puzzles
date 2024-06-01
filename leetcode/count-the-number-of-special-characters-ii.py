class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lcases = list(set({e.lower() for e in word}))
        s = 0
        for e in lcases:
            if e not in word or e.upper() not in word:
                continue
            if word.rfind(e) < word.index(e.upper()):
                s += 1
        return s
