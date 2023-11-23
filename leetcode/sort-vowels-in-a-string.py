class Solution:
    def sortVowels(self, s: str) -> str:
        v = ['a', 'e', 'i', 'o', 'u']
        v = [e.upper() for e in v] + v
        zet = set(v)
        vs = []
        for _, e in enumerate(s):
            if e in zet:
                vs.append(e)
        vs.sort()
        ret = []
        i = 0
        for j, e in enumerate(s):
            if e in zet:
                ret.append(vs[i])
                i += 1
            else:
                ret.append(s[j])
        return "".join(ret)
