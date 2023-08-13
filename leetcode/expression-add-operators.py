class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        from itertools import product
        f = lambda x, y: x + y
        g = lambda x, y: x - y
        h = lambda x, y: x * y
        q = lambda x, y: int((str(x) + str(y)))
        def print_(oplist):
            fst = [num[0]]
            for i in range(len(num) - 1):
                e = oplist[i]
                if e == f:
                    fst.append("+")
                elif e == g:
                    fst.append("-")
                elif e == h:
                    fst.append("*")
                else:
                    if fst[-1] == "0" and (len(fst) == 1 or fst[-2] in ["+", "-", "*"]): #accept 1000... reject 0100 ...
                        return "2**31"
                fst.append(num[i + 1])
            return "".join(fst)
        ns = [int(e) for e in num]
        n = len(ns)
        rets = []
        for fgh in product([f, g, h, q], repeat = n - 1):
            if eval(print_(fgh)) == target:
                rets.append(print_(fgh))
        return [r for r in rets if r != "2**31"]
