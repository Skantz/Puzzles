class Solution:
    def findComplement(self, num: int) -> int:
        n = num.bit_length()
        return num ^ (2**n - 1)
