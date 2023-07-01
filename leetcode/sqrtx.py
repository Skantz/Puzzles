class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        xa = x/2
        for _ in range(20):
            xa = 0.5 * (xa + x / xa)
        return int(xa)
