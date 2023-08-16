class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        assert(root)
        s = list([root])
        bl = root.val
        while s or z:
            if not s:
                s = [e for e in z]
            bl = s[0].val
            z = []
            for e in s:
                if e.left:
                    z.append(e.left)
                if e.right:
                    z.append(e.right)
            s = []
        return bl
