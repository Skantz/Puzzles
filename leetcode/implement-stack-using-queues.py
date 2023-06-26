class MyStack:

    def __init__(self):
        self.q1 = list()

    def push(self, x: int) -> None:
        return self.q1.append(x)

    def pop(self) -> int:
        return self.q1.pop()

    def top(self) -> int:
        return self.q1[-1]

    def empty(self) -> bool:
        return not self.q1
