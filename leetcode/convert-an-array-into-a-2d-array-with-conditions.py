class Solution:
    def findMatrix(self, nums):
        nums = sorted(nums)[::-1]
        ret = []
        for i, e in enumerate(nums):
            changed = False
            for i, g in enumerate(ret):
                ret[i] = g + [e] if not e in g else g
                changed = True if e not in g else False
                if changed:
                    break
            ret = ret + [[e]] if not changed else ret
        return ret
