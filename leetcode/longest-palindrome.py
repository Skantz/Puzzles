class Solution:
    def longestPalindrome(self, s: str) -> int: from collections import Counter; return (lambda c: sum(c[e] - (1 if c[e] % 2 else 0) for e in c) + (1 if any(c[e] for e in c if c[e] % 2) else 0))(Counter(s))
