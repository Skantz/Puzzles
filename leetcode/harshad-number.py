class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        def f(x): return map(int, list(str(x)))
        return sum(f(x)) if x % sum(f(x)) == 0 else -1
