class Solution:
    def isValidBST(self, root: Optional[TreeNode], range=(-2**31 - 1, 2**31 + 1)) -> bool:
        if not root:
            return True
        if root.val <= range[0] or range[1] <= root.val:
            return False
        c1 = self.isValidBST(root.left, (range[0], root.val))
        return c1 and self.isValidBST(root.right, (root.val, range[1]))
