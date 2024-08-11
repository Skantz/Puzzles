class Solution:
    def rearrangeArray(self, nums):
        a = (n for n in nums if n < 0)
        b = (n for n in nums if not n < 0)
        return list(e for f in zip(b, a) for e in f)
