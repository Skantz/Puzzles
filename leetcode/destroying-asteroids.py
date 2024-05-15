from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for (i, e) in enumerate(asteroids):
            if mass < e:
                return False
            mass += e
        return True
