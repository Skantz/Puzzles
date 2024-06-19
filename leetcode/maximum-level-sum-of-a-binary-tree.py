from typing import Optional


class TreeNode:
    def __init__(self, val: int, right, left):
        self.right = right
        self.val = val
        self.left = left


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
        s = [root]
        z = []
        max_sum = root.val
        max_sum_level = 0
        c = 0
        # level-order traversal
        while s or z:
            if not s:
                c += 1
                s = z[:]
                z = []
                if sum([e.val for e in s]) > max_sum:
                    max_sum = sum([e.val for e in s])
                    max_sum_level = c
            a = s.pop(0)
            if a.left:
                z.append(a.left)
            if a.right:
                z.append(a.right)
        return max_sum_level + 1
