class Solution:
    def isSymmetric_(self, left, right) -> bool:
        if not left or not right:
            return left == right
        return left.val == right.val \
          and self.isSymmetric_(left.left, right.right) \
          and self.isSymmetric_(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetric_(root.left, root.right)
