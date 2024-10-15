class Solution:
    def reorderSpaces(self, text: str) -> str:
        s = text.count(' ')
        text = text.split(' ')
        text = [e for e in text if e.isalpha()]
        n = len(text) - 1
        ret = ""
        for e in text:
            ret += e
            ret += ' ' * (s // n) if n else ""
        ret = ret.rstrip(' ')
        if not n or (s % n):
            ret += ' ' * ((s % n) if n else s)
        return ret
