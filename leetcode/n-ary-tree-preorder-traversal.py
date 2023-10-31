class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        res = []
        for c in root.children:
            res.extend(self.preorder(c))
        return [root.val] + res
