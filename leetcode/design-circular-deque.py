class MyCircularDeque:

    def __init__(self, k: int):
        self.s = k
        self.q = []

    def insertFront(self, value: int) -> bool:
        if len(self.q) < self.s:
            self.q = [value] + self.q
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.q) < self.s:
            self.q.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if self.q:
            self.q = self.q[1:]
            return True
        return False

    def deleteLast(self) -> bool:
        if self.q:
            self.q = self.q[:-1]
            return True
        return False

    def getFront(self) -> int:
        if not self.q:
            return -1
        return self.q[0]

    def getRear(self) -> int:
        if not self.q:
            return -1
        return self.q[-1]

    def isEmpty(self) -> bool:
        return not self.q

    def isFull(self) -> bool:
        return len(self.q) == self.s
