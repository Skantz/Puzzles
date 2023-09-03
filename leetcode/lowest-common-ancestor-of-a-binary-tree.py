class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode', d=0) -> 'TreeNode':
        if not root:
            return None
        t = p if root.val == p.val else q if root.val == q.val else None
        l = self.lowestCommonAncestor(root.left, p, q, d + 1)
        r = self.lowestCommonAncestor(root.right, p, q, d + 1)
        if t:
            return t
        if l and r:
            return root
        return l if l else r
