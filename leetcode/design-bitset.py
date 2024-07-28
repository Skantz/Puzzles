class Bitset:

    def __init__(self, size: int):
        self.n = size
        self.ns = {e for e in range(self.n)}
        self.zs = set()

    def fix(self, idx: int) -> None:
        if idx in self.ns: self.ns.remove(idx)
        self.zs.add(idx)

    def unfix(self, idx: int) -> None:
        if idx in self.zs: self.zs.remove(idx)
        self.ns.add(idx)

    def flip(self) -> None:
        self.zs, self.ns = self.ns, self.zs

    def all(self) -> bool:
        return not bool(self.ns)

    def one(self) -> bool:
        return bool(self.zs)

    def count(self) -> int:
        return len(self.zs)

    def toString(self) -> str:
        return "".join('1' if i in self.zs else '0' for i in range(self.n))
