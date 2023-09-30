class Solution:
    def sum(self, root) -> int:
        if not root:
            return 0
        return root.val + self.sum(root.left) + self.sum(root.right)

    def findTilt(self, root) -> int:
        if not root:
            return 0
        s = abs(self.sum(root.left) - self.sum(root.right))
        return s + self.findTilt(root.left) + self.findTilt(root.right)
