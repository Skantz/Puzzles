class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        assert(len(s) == len(indices))
        res = ["X"]*len(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return "".join(res)
