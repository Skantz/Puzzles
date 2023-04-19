class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a = [n for n in nums if n < 0]
        b = [n for n in nums if not n < 0]
        c = []
        for i in range(len(b)):
            c.append(b[i])
            c.append(a[i])
        return c
