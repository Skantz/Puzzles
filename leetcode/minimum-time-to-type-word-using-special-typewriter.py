class Solution:
    def minTimeToType(self, word: str) -> int:
        s = 0
        p = 'a'
        for e in word:
            if e != p:
                s += min(abs(ord(e) - ord(p)), 26 - abs(ord(p) - ord(e)))
            s += 1
            p = e
        return s
