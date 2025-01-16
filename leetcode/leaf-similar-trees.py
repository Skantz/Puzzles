class Solution:
    def leafSimilar(self, rx, ry) -> bool:
        def collect(r, c):
            if not r:
                return
            if not r.left and not r.right:
                c.append(r.val)
            left = collect(r.left, c)
            right = collect(r.right, c)
            return
        xs = []
        ys = []
        collect(rx, xs)
        collect(ry, ys)
        return xs == ys
