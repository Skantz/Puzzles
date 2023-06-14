class Solution:
    def sumOfLeftLeaves_(self, root: Optional[TreeNode], is_left) -> int:
        if not root:
            return 0
        if not root.left and not root.right and is_left:
            return root.val
        return self.sumOfLeftLeaves_(root.left, True) \
          + self.sumOfLeftLeaves_(root.right, False)
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.sumOfLeftLeaves_(root, False)
