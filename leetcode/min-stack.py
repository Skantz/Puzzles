class MinStack:

    def __init__(self):
        self.min = []
        self.min_run = []

    def push(self, val: int) -> None:
        self.min.append(val)
        self.min_run.append(min(val, self.min_run[-1]) if self.min_run else val)

    def pop(self) -> None:
        self.min.pop(-1)
        self.min_run.pop(-1)

    def top(self) -> int:
        return self.min[-1]

    def getMin(self) -> int:
        return self.min_run[-1]
