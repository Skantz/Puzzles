class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.split(' ')
        text = " ".join(sorted(text, key=lambda x: len(x)))
        text = text[0].upper() + text[1:]
        text = text[0] + "".join(e.lower() for e in text[1:])
        return text
