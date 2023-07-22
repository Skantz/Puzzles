class Solution:
    def goodNodes(self, root: TreeNode, rootval=-10**5 - 1) -> int:
        if not root:
            return 0
        v = root.val
        if v >= rootval:
            return 1 + self.goodNodes(root.left, v) + self.goodNodes(root.right, v)
        else:
            return self.goodNodes(root.left, rootval) + self.goodNodes(root.right, rootval)
