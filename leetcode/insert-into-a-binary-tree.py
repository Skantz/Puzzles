from typing import Optional


class TreeNode:
    def __init__(self, V=0, L=None, R=None):
        self.V = V
        self.L = L
        self.R = R


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val, None, None)
        assert root.V != val
        f = self.insertIntoBST
        new = TreeNode(val, None, None)
        if val < root.V:
            if root.L:
                _ = f(root.L, val)
            else:
                root.L = new
        elif val > root.V:
            if root.R:
                _ = f(root.R, val)
            else:
                root.R = new
        return root
