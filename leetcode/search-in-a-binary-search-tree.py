class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        left = self.searchBST(root.left, val)
        if left:
            return left
        right = self.searchBST(root.right, val)
        if right:
            return right
        return None
