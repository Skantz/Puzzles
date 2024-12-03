class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        ret = []
        def d(x): return [int(e) for e in list(str(x))]
        for n in range(left, right + 1):
            ret = ret + [n] if all(n % s == 0 if s != 0 else False for s in d(n)) else ret
        return ret
