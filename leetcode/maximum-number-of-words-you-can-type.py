class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        sm = 0
        for s in text.split(" "):
            if any(e in s for e in brokenLetters):
                continue
            sm += 1
        return sm
