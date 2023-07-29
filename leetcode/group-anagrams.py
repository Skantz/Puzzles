class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        kv = {}
        for s in strs:
            try:
                kv["".join(sorted(s))] += [s]
            except KeyError:
                kv["".join(sorted(s))] = [s]
        return [kv[e] for e in kv]
