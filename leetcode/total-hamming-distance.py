from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        r = max([e.bit_length() for e in nums])
        s, b = 0, 1
        for i in range(r):
            c1 = sum([(e & b) >> i for e in nums])
            c2 = sum([((e & b) >> i) ^ 1 for e in nums])
            s += c1 * c2
            b <<= 1
        return s
