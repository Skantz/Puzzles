class Solution:

    def depth(self, head):
        if not head:
            return 0
        return 1 + max(self.depth(head.left), self.depth(head.right))

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        if self.depth(root.left) == self.depth(root.right):
            return root
        if self.depth(root.left) > self.depth(root.right):
            return self.lcaDeepestLeaves(root.left)
        return self.lcaDeepestLeaves(root.right)
