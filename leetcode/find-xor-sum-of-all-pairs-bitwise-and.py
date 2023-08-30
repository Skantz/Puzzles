class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        # logical and distributes : (a & b) ^ (a & d) = a & (b ^ d)
        arr1_fst = arr1[0]
        arr2_fst = arr2[0]
        arr2_xor = arr2_fst
        for e in (arr2[1:]):
            arr2_xor ^= e
        all_and = arr1_fst & arr2_xor
        for e in (arr1[1:]):
            all_and ^= (e & arr2_xor)
        return all_and
