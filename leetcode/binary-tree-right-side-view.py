class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        s = list([root])
        bl = root.val
        z = []
        ret = []
        while s or z:
            if not s:
                s = z[:]
            bl = s[0].val
            z = []
            for e in s:
                if e.left:
                    z.append(e.left)
                if e.right:
                    z.append(e.right)
            ret.append([s_.val for s_ in s])
            s = []
        return [z_[-1] for z_ in ret]
