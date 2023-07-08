class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        d = [int(i) for i in list(str(n))]
        s = 1
        for e in d:
            s *= e
        return s - sum(d)
