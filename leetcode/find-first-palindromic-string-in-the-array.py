class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        try:
            return next(e for e in words if e[:len(e)//2] == e[::-1][:len(e)//2])
        except StopIteration:
            return ""
