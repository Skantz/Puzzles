class Solution:
    def connect(self, root):
        q = list()
        q.append(root)
        q_p = list()
        while q:
            p = None
            for e in q:
                if not e:
                    continue
                if p:
                    p.next = e
                if e.left:
                    q_p.append(e.left)
                if e.right:
                    q_p.append(e.right)
                p = e
            q = list(q_p)
            q_p = list()
        return root
