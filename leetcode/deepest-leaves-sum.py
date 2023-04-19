class Solution:
    def calcDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.calcDepth(root.left), self.calcDepth(root.right))
    def deepestLeaveSumPrime(self, root: Optional[TreeNode], curr_d : int, max_d : int):
        if curr_d >= max_d and root:
            return [root.val]
        if not root:
            return []
        return self.deepestLeaveSumPrime(root.left, curr_d + 1, max_d) + self.deepestLeaveSumPrime(root.right, curr_d + 1, max_d)
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        depth = self.calcDepth(root)
        if depth == 0:
            return 0
        if depth == 1:
            return root.val
        else:
            return sum(self.deepestLeaveSumPrime(root, 1, depth))
