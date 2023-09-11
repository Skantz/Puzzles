class Solution:
    def stoneGame_(self, piles: List[int]) -> bool:
        piles = sorted(piles)[::-1]
        return sum(piles[::2]) >= sum(piles[1::2])
    def stoneGame(self, piles: List[int]) -> bool:
        return True
