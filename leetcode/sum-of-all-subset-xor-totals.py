def powerset(lst):
    if not lst:
        return [[]]
    pw = powerset(lst[1:])
    return pw + ([[lst[0]] + e for e in pw])

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        s = 0
        for i in powerset(nums):
            l = list(i)
            if not l:
                continue
            s_ = l[0]
            for e in l[1:]:
                s_ ^= e
            s += s_
        return s
