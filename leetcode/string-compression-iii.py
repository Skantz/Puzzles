class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        while word:
            w = word[0]
            i = 0
            while i < min(9, len(word)) and word[i] == w:
                i += 1
            word = word[i:]
            comp += str(i) + w
        return comp
