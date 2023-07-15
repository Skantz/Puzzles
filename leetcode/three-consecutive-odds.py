class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            a = True
            for j in range(i, i + 3):
                if arr[j] % 2 == 0:
                    a = False
            if a:
                return True
        return False
