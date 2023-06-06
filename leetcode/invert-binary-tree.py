class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        left_ = self.invertTree(root.right)
        right_ = self.invertTree(root.left)
        root.left = left_
        root.right = right_
        return root
