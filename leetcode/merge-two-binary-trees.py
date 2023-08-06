class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        m = TreeNode()
        if root1 and root2:
            m.val = root1.val + root2.val
            m.left = self.mergeTrees(root1.left, root2.left)
            m.right = self.mergeTrees(root1.right, root2.right)
        elif root1:
            m.val = root1.val
            m.left = self.mergeTrees(root1.left, None)
            m.right = self.mergeTrees(root1.right, None)
        elif root2:
            m.val = root2.val
            m.left = self.mergeTrees(None, root2.left)
            m.right = self.mergeTrees(None, root2.right)
        return m
