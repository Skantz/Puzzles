class Solution:
    def getTargetCopy(self, original, cloned, target):
        assert(~((original is None) ^ (cloned is None)) and target)
        if not original:
            return None
        if original == target:
            return cloned
        f = self.getTargetCopy
        left = f(original.left, cloned.left, target)
        return left if left else f(original.right, cloned.right, target)
