class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        assert(root)
        if q.val < p.val:
            p, q = q, p
        if root.val == p.val:
            return p
        elif root.val == q.val:
            return q
        if p.val < root.val and root.val < q.val:
            return root
        else:
            if root.val > q.val:
                return self.lowestCommonAncestor(root.left, p, q)
            return self.lowestCommonAncestor(root.right, p, q)
