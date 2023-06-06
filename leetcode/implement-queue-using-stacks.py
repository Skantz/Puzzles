class MyQueue:

    def __init__(self):
        self.list = list()

    def push(self, x: int) -> None:
        self.list.append(x)

    def pop(self) -> int:
        x = self.list[0]
        self.list.remove(x)
        return x

    def peek(self) -> int:
        return self.list[0]

    def empty(self) -> bool:
        return not self.list
