class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        assert(~((original is None) ^ (cloned is None)) and target)
        if not original:
            return None
        if original == target:
            return cloned
        left = self.getTargetCopy(original.left, cloned.left, target)
        return left if left else self.getTargetCopy(original.right, cloned.right, target)
