class Solution:
    def isSymmetric_(self, left, right) -> bool:
        if not l or not r:
            return l == r
        return left.val == right.val \
          and self.isSymmetric_(left.left, right.right) \
          and self.isSymmetric_(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetric_(root.left, root.right)
