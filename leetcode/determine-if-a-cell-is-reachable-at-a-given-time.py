class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x_d = abs(sx - fx)
        y_d = abs(sy - fy)
        xy_d = abs(x_d - y_d)
        min_moves = xy_d + max(x_d - xy_d, y_d - xy_d)
        if t < min_moves:
            return False
        if min_moves < 1 and 0 < t < 2:
            return False
        return True
