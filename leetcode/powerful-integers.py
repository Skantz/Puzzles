class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int):
        xs = []
        if 1 < x:
            i = 0
            while x**i - 1 < bound:
                xs.append(x**i)
                i += 1
        else:
            xs = [1]
        ys = []
        if 1 < y:
            j = 0
            while y**j - 1 < bound:
                ys.append(y ** j)
                j += 1
        else:
            ys = [1]
        rets = []
        for e in xs:
            for g in ys:
                if e + g - 1 < bound:
                    rets.append(e + g)
        return list(set(rets))
