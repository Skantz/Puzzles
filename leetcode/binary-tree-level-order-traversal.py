class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        s = [root]
        z = []
        ret = [[]]
        while s or z:
            if not s:
                s = [e for e in z]
                z = []
                ret.append([])
            a = s.pop(0)
            ret[-1].append(a.val)
            if a.left:
                z.append(a.left)
            if a.right:
                z.append(a.right)
        return ret
