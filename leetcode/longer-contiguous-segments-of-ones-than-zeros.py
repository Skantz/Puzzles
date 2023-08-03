class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        try:
            return sorted(s).index('1') < len(s)/2
        except ValueError:
            return False
