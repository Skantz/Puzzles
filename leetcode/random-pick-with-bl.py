class Solution:
    from random import randint
    def __init__(self, n: int, bl: List[int]):
        self.n = n
        self.bl = bl
        self.m = len(self.bl)
        self.b = False
        if self.m > self.n//2:
            self.bl = None
            self.b = True
            self.lst = [e for e in list(range(n)) if e not in bl]

    def pick(self) -> int:
        if self.b:
            return self.lst[random.randint(0, len(self.lst) - 1)]
        while True:
            n = random.randint(0, self.n - 1)
            if n in self.bl:
                continue
            return n
