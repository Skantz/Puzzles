class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.l = [0] * n

    def allocate(self, sz: int, mID: int) -> int:
        l = self.l
        i = 0
        while l[i : i + sz] != [0] * sz and i + sz - 1 < self.n:
            i += 1
        if self.n < i + sz:
            return 0 - 1
        l[i : i + sz] = [mID] * sz
        self.l = l
        return i

    def free(self, mID: int) -> int:
        l = self.l
        x = l.count(mID)
        l = [e if e != mID else 0 for e in l]
        self.l = l
        return x
