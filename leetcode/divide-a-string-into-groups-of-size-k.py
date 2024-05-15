from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ret = [s[i:i + k] for i in range(0, len(s), k)]
        ret[-1] = ret[-1] + ((k - (len(s) % k)) % k) * fill
        return ret
