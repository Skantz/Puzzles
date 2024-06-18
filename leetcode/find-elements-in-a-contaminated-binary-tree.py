from typing import Optional


class TreeNode:
    def __init__(self, v=0, left=None, right=None):
        self.left = left
        self.right = right
        self.v = v


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.vs = set()
        self.root = self.go(root, 0)

    def go(self, root: Optional[TreeNode], v: int):
        if not root:
            return None
        root.v = v
        self.vs.add(v)
        root.left = self.go(root.left, v * 2 + 1)
        root.right = self.go(root.right, v * 2 + 2)
        return root

    def find(self, target: int) -> bool:
        return target in self.vs
