class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.strip().split()
        a = [b for b in a if len(b) > 0][::-1]
        return " ".join(a)
