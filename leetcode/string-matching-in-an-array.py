from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ret = []
        for w in words:
            s = "#".join([v for v in words if v != w])
            if w in s:
                ret.append(w)
        return ret
