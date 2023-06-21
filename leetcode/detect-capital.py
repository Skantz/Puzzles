class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        ords = [ord(s) for s in word]
        a = all(i >= 97 for i in ords)
        b = all(i >= 97 for i in ords[1:])
        c = all(i < 97 for i in ords)
        return a or (b and ords[0] < 97) or c if word else True
