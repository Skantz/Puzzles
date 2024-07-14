from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 1:
            return []
        if n < 2:
            return ["()"]
        prev = self.generateParenthesis(n - 1)
        rets = {'(' + e + ')' for e in prev}
        for e in prev:
            for i in range(len(prev)):
                rets.add(e[:i] + "()" + e[i:])
        return rets
