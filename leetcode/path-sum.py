from typing import Optional


class TreeNode:
    def __init__(self, x=None, y=None, z=0):
        self.val = z
        self.right = x
        self.left = y


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], t: int) -> bool:
        if not root:
            return False
        return self.has_path_sum(root, t)

    def has_path_sum(self, root: Optional[TreeNode], t: int) -> bool:
        f = self.has_path_sum
        if not root:
            return t == 0
        if not root.left and not root.right:
            return root.val == t
        left = f(root.left, t - root.val) if root.left else False
        right = f(root.right, t - root.val) if root.right else False
        return (left | right)
