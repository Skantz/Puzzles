class Solution:
    def finalPositionOfSnake(self, n: int, commands) -> int:
        x = sum(1 for e in commands if e == "RIGHT")  + sum(0 - 1 for e in commands if e == "LEFT")
        y = sum(0 - 1 for e in commands if e == "UP") + sum(1 for e in commands if e == "DOWN")
        return y * n + x
