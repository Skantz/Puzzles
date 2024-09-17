from functools import cache


class Solution:
    @cache
    def sumNumbers(self, root, carry="") -> int:
        if not root:
            return 0
        v = str(root.val)
        if not root.left and not root.right:
            return int(carry + v)
        f = self.sumNumbers
        left = f(root.left, carry + v)
        right = f(root.right, carry + v)
        return left + right
