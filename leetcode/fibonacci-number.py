class Solution:
    def fib(self, n: int) -> int:
        """
        match n:
            case 0 | 1:
                return n
            case _:
                return self.fib(n - 1) + self.fib(n - 2)
        """
        y = (1 + 5 ** 0.5) / 2
        z = (y ** n) - ((0 - y) ** (0 - n))
        return int(z // 5 ** 0.5)
