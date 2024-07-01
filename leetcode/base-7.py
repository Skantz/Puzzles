class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        out = ""
        s = 1
        if num < 0:
            num = - num
            s = - 1
        while num > 0:
            out = out + str(num % 7)
            num = num // 7
        return out[::-1] if s > 0 else "-" + out[::-1]
