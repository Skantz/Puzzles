from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 1:
            return []
        if n < 2:
            return ["()"]
        rets = set()
        m = (n - 1) * 2
        for e in self.generateParenthesis(n - 1):
            rets.add('(' + e + ')')
            for i in range(m):
                rets.add(e[:i] + "()" + e[i:])
        return rets
