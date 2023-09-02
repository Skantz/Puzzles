class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        s = [root]
        z = []
        odd = False
        while s:
            maxx = 0
            minn = 10**6 + 1
            while s:
                e = s.pop(0)
                if odd:
                    if e.val >= minn or (e.val % 2):
                        return False
                    minn = min(minn, e.val)
                else:
                    if e.val <= maxx or (not e.val % 2):
                        return False
                    maxx = max(maxx, e.val)
                if e.left:
                    z.append(e.left)
                if e.right:
                    z.append(e.right)
            odd = False if odd else True
            s = z[:]
            z = []
        return True
