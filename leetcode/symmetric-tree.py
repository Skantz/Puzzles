class Solution:
    def isSymmetric_(self, left, right) -> bool:
        if left == None:
            return right == None
        if right == None:
            return left == None
        return left.val == right.val \
          and self.isSymmetric_(left.left, right.right) \
          and self.isSymmetric_(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isSymmetric_(root.left, root.right)
