class Solution:
    def groupAnagrams(self, strs):
        ret = {}
        for e in strs:
            f = "".join(sorted(e))
            ret[f] = ret[f] + [e] if f in ret else [e]
        return list(ret.values())
