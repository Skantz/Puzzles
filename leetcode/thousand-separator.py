class Solution:
    def thousandSeparator(self, n: int) -> str:
        return "".join(e + ("." if ((len(str(n)) - i - 1) % 3 == 0 and i < len(str(n)) - 1) else "") for i, e in enumerate(list(str(n))))
