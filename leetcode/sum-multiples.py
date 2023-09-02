class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return(sum(list(set(list(range(0, n + 1, 3)) + list(range(0, n + 1, 5)) + list(range(0, n + 1, 7))))))
