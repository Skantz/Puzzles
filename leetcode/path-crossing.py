class Solution:
    def isPathCrossing(self, path: str) -> bool:
        u, r = 0, 0
        vis = {(0, 0)}
        for e in path:
            u += 1 if e == "N" else -1 if e == "S" else 0
            r += 1 if e == "E" else -1 if e == "W" else 0
            if (u, r) in vis:
                return True
            vis.add((u, r))
        return False
