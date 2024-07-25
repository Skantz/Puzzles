from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ret = []
        i = 0
        j = 1
        while i < len(target):
            if target[i] != j:
                ret.append("Push")
                ret.append("Pop")
            else:
                ret.append("Push")
                i += 1
            j += 1
        return ret
