class Solution:
    def isValidBST(self, root: Optional[TreeNode], rang=(-2**31 - 1, 2**31 + 1)) -> bool:
        if not root:
            return True
        if root.val <= rang[0] or rang[1] <= root.val:
            return False
        c1 = self.isValidBST(root.left, (rang[0], root.val))
        return c1 and self.isValidBST(root.right, (root.val, rang[1]))
