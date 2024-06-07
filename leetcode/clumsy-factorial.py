class Solution:
    def clumsy(self, n: int) -> int:
        if n < 1:
            return 0
        op = {0: "*", 1: "//", 2: "+", 3: "-"}
        s = str(n)
        for i in range(n - 1, 0, -1):
            s += " " + op[(n - i - 1) % 4] + str(i)
        return eval(s)
