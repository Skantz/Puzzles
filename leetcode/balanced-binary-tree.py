class Solution:
    def depth(self, root):
        if not root:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 \
          and self.isBalanced(root.left) and self.isBalanced(root.right)
