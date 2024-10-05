class Solution:
    def goodNodes(self, root, rootval=-10**5 - 1) -> int:
        if not root:
            return 0
        v = root.val
        f = self.goodNodes
        if v >= rootval:
            return 1 + f(root.left, v) + f(root.right, v)
        return f(root.left, rootval) + f(root.right, rootval)
