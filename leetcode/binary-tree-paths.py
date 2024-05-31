from typing import Optional, List


class TreeNode:
    def __init__(self, v=0, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        btp = self.binaryTreePaths
        if not root:
            return []
        if not (root.left or root.right):
            return [str(root.val)]
        left = btp(root.left)
        right = btp(root.right)
        prefix = str(root.val) + "->"
        return [prefix + l for l in left] + [prefix + r for r in right]
