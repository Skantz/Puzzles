class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return str(1 + int("".join([str(e) for e in digits])))
