class Solution:
    def minBitFlips(self, x: int, y: int) -> int:
        return (x ^ y).bit_count()
