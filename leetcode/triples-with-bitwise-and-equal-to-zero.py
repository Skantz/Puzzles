class Solution:
    def countTriplets(self, nums) -> int:
        c = {}
        for _, e in enumerate(nums):
            for _, f in enumerate(nums):
                s = c[e & f] + 1 if e & f in c else 1
                c[e & f] = s
        ret = 0
        for e in nums:
            for f in c:
                s = c[f] if not e & f else 0
                ret += s
        return ret
