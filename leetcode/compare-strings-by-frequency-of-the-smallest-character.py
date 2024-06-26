from typing import List
from bisect import bisect_right


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        ret = []
        words.sort(key=lambda x: x.count(min(x)))
        for e in queries:
            ret.append(len(words) - bisect_right(words, e.count(min(e)), key=lambda x: x.count(min(x))))
        return ret
