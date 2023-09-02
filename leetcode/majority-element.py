class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapp = {}
        for n in nums:
            try:
                mapp[n] += 1
            except KeyError:
                mapp[n] = 1
        maxx = max(mapp.values())
        return next(k for (k, e) in mapp.items() if e == maxx)
