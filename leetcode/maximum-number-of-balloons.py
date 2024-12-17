class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        c = Counter(text)
        b = not all(e in c.keys() for e in "aobln")
        return 0 if b else min(min([c[e] for e in c if e in 'abn']), min([c[e] // 2 for e in c if e in 'ol']))
