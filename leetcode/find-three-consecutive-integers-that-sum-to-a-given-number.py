class Solution:
    def sumOfThree(self, num: int):
        if num % 3:
            return []
        x = num // 3
        return [x - 1, x, x + 1]
