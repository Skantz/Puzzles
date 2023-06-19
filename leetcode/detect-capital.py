class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if not word:
            return True
        ords = [ord(s) for s in word]
        a = not False in [i >= 97 for i in ords]
        b = ords[0] < 97 and not False in [i >= 97 for i in ords[1:]]
        c = not False in [i < 97 for i in ords]
        return a or b or c
