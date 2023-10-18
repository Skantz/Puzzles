class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def flatten(n):
            if not n:
                return []
            return [n.val] + flatten(n.left) + flatten(n.right)
        lst = flatten(root)
        lst.sort()
        return lst[k - 1]
