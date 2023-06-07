class Solution:
    def countDigits(self, num: int) -> int:
        return sum([1 if (num % int(i) == 0) else 0 for i in str(num)])
