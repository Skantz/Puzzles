class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        max_ = 1
        for c in root.children:
            max_ = max(1 + self.maxDepth(c), max_)
        return max_
