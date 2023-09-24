class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def has_k(n):
            return True if bin(n).count("1") == k else False
        return sum([n for i, n in enumerate(nums) if has_k(i)])
