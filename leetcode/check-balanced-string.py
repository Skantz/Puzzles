class Solution:
    def isBalanced(self, num: str) -> bool:
        x = num[::2]
        y = num[1::2]
        return sum(int(e) for e in x) == sum(int(e) for e in y)
