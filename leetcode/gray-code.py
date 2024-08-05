from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n < 1:
            return []
        if n < 2:
            return [0, 1]
        f = self.grayCode
        prev = f(n - 1)
        ret1, ret2 = [], []
        for e in prev:
            ret1.append(bin(e)[2:] + '0')
            ret2.append(bin(e)[2:] + '1')
        return list(map(lambda x: int(x, 2), ret1 + ret2[::-1]))
