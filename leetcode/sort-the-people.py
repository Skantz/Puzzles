class Solution:
    def sortPeople(self, ns, hs):
        x = sorted(zip(hs, ns))
        return (e[1] for e in x[::-1])
