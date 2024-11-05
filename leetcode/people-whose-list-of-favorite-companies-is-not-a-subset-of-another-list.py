class Solution:
    def peopleIndexes(self, xss):
        n = len(xss)
        ret = []
        xs = [set(e) for e in xss]
        for i in range(n):
            brk = False
            for j in range(n):
                if i == j:
                    continue
                if xs[i] - xs[j] == set():
                    brk = True
                    break
            if brk:
                continue
            ret.append(i)
        return ret
