class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) <= 1:
            return num
        return self.addDigits(sum(int(i) for i in list(str(num))))
