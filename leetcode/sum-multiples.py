class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return(sum(list(set([i for i in range(0, n + 1, 3)] + [j for j in range(0, n + 1, 5)] + [k for k in range(0, n + 1, 7)]))))
