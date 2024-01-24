from itertools import groupby


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        tmp = [list(c[1])
               for c in groupby(list(word), lambda c: c.isalpha())
               if not c[0]]
        tmp = [int(''.join(e)) for e in tmp]
        return len(set(tmp))
