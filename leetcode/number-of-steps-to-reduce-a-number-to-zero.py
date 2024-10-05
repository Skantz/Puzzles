class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num < 1:
            return 0
        f = self.numberOfSteps
        if num % 2 == 0:
            return 1 + f(num // 2)
        return 1 + f(num - 1)
