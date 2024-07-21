class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if ord(num[i]) % 2:
                i += 1
                break
        return num[:i]
