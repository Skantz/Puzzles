class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        left_ = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        root.left = left_
        return root
