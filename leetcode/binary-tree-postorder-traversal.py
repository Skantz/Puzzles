class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [] if not root else self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
