from typing import Any, List


class Solution:
    def findSolution(self, f: Any, z: int) -> List[List[int]]:
        ret = []
        for x in range(1, 1000):
            for y in range(1, 1000):
                w = f.f(x, y)
                if z < w:
                    break
                if w == z:
                    ret.append([x, y])
        return ret
