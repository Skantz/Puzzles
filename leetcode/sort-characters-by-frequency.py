class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        c = Counter(s)
        return "".join(sorted(list(s), key=lambda x: (c[x], ord(x)), reverse=True))
