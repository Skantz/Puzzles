class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            a = True
            for j in range(i, i + 3):
                try:
                    if arr[j] % 2 == 0:
                        a = False
                except IndexError:
                    return False
            if a:
                return True
        return False
