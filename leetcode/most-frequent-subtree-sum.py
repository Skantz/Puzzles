class Solution:
    def findFrequentTreeSum(self, root):
        c = {}
        def collect(x):
            if not x:
                return 0
            if not x.left and not x.right:
                c[x.val] = c[x.val] + 1 if x.val in c else 1
                return x.val
            left  = collect(x.left)
            right = collect(x.right)
            y = x.val
            z = left + right + y
            c[z] = c[z] + 1 if z in c else 1
            return z
        collect(root)
        return [i for i in c if c[i] == max(c.values())]
