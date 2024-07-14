from typing import List


map_ = {1: []}

for i in range(2, 8):
    def basef(x): return chr(97 + (i - 2) * 3 + x)
    map_[i] = [basef(0), basef(1), basef(2)]

map_[7].append('s')

for i in range(8, 10):
    def basef(x): return chr(97 + (i - 2) * 3 + x + 1)
    map_[i] = [basef(0), basef(1), basef(2)]

map_[9].append('z')


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n < 1:
            return []
        if n < 2:
            return map_[int(digits[0])]
        prev = self.letterCombinations(digits[1:])
        x = digits[0]
        rets = []
        for e in prev:
            for f in map_[int(x)]:
                rets.append(f + e)
        return rets
