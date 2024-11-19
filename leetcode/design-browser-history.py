class BrowserHistory:

    def __init__(self, hp: str):
        self.h = [hp]
        self.c = 0

    def visit(self, url: str) -> None:
        self.h = self.h[: self.c + 1]
        self.h.append(url)
        self.c = len(self.h) - 1

    def back(self, steps: int) -> str:
        self.c = self.c - steps
        if self.c < 0:
            self.c = 0
        return self.h[self.c]

    def forward(self, steps: int) -> str:
        self.c = self.c + steps
        if len(self.h) - 1 < self.c:
            self.c = len(self.h) - 1
        return self.h[self.c]
