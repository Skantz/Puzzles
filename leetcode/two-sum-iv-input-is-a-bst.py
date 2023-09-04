class Solution:

    bigroot = None

    def is_in_tree(self, root, k: int, nomatch=None) -> bool:
        if not root:
            return False
        if root.val == k and root != nomatch:
            return True
        return self.is_in_tree(root.left, k, nomatch) or self.is_in_tree(root.right, k, nomatch)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not self.bigroot:
            self.bigroot = root
        if not root:
            return False
        return self.is_in_tree(self.bigroot.left, k - root.val, root) \
          or self.is_in_tree(self.bigroot.right, k - root.val, root) \
          or self.findTarget(root.left, k) \
          or self.findTarget(root.right, k)
