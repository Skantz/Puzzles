from typing import List


class Solution:
    def replaceWords(self, x: List[str], y: str) -> str:
        x.sort()
        y = y.split(" ")
        y_p = y
        y = y + [[]]
        while y_p != y:
            y = y_p
            for i, e in enumerate(y_p):
                for f in x:
                    if f in e and e[:len(f)] == f:
                        y_p[i] = f
                        break
        return " ".join(y_p)
