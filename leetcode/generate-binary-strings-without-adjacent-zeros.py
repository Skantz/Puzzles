class Solution:
    def validStrings(self, n: int):
        if n < 1:
            return []
        if n < 2:
            return ['0', '1']
        f = self.validStrings
        prev = f(n - 1)
        rets = []
        for e in prev:
            rets.append(e + '1')
            if e[-1] == '1':
                rets.append(e + '0')
        return rets
