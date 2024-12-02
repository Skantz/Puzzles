class Solution:
    def numberOfWeakCharacters(self, xss):
        ret = 0
        ub = 0
        xss.sort(key = lambda x: (0 - x[0], x[1]))
        for (_, x) in xss:
            ret = ret + 1 if x < ub else ret
            ub = x if ub < x else ub
        return ret
