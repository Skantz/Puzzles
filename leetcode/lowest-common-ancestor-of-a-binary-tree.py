class Solution:
    def lowestCommonAncestor(self, root, p, q, d=0):
        if not root:
            return None
        t = p if root.val == p.val else q if root.val == q.val else None
        f = self.lowestCommonAncestor
        l = f(root.left, p, q, d + 1)
        r = f(root.right, p, q, d + 1)
        if t:
            return t
        if l and r:
            return root
        return l if l else r
