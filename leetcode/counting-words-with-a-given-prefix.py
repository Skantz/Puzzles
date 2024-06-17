from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        return len([w for w in words if w[:n] == pref])
