class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = "".join([i for i in s if i.isalnum()]).lower()
        return ss == ss[::-1]
