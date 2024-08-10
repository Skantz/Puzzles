class Solution:
    #@cache
    def isSameTree(self, p, q) -> bool:
        if not (p and q): return not (p or q)
        f = self.isSameTree
        return p.val == q.val and f(p.left, q.left) and f(p.right, q.right)
