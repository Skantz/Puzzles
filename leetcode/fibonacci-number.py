class Solution:
    def fib(self, n: int) -> int:
        match n:
            case 0 | 1:
                return n
            case _:
                return self.fib(n - 1) + self.fib(n - 2)
