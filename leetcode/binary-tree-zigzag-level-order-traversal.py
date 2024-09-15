class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        s = list([root])
        bl = [[root]]
        z = []
        sgn = 0
        while s or z:
            if not s:
                s = z[:]
            z = []
            for e in s:
                if e.left:
                    z.append(e.left)
                if e.right:
                    z.append(e.right)
            if z:
                bl.append(z[::-1] if not sgn else z)
            s = []
            sgn = sgn ^ 1
        bl = [[e.val for e in f] for f in bl]
        return bl
