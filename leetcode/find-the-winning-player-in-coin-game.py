class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        if x < 1 or y < 4:
            return "Bob"
        if x < 2 or y < 8:
            return "Alice"
        f = self.losingPlayer
        rec = f(x - 2, y - 8)
        return rec
