class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        return [int.bit_count(n & 1365), int.bit_count(n & 2730)]
