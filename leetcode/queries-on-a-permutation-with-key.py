class Solution:
    def processQueries(self, queries, m: int):
        P = list(range(1, m + 1))
        ret = []
        for e in queries:
            i = P.index(e)
            ret.append(i)
            P = [e] + P[:i] + P[i + 1:]
        return ret
