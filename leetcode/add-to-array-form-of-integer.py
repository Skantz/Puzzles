class Solution:
    def addToArrayForm(self, num, k: int):
        from os import sys
        sys.set_int_max_str_digits(10**4 + 1)
        return [int(e) for e in (str(int("".join([str(e) for e in num])) + k))]
