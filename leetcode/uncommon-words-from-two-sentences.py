class Solution:
    def uncommonFromSentences(self, s1: str, s2: str):
        s1 = s1.split()
        s2 = s2.split()
        return [e for e in s1 if not e in s2 and s1.count(e) < 2] + [e for e in s2 if not e in s1 and s2.count(e) < 2]
