class Foo:
    def __init__(self):
        pass

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.first = True

    def second(self, printSecond: 'Callable[[], None]') -> None:
        if self.first:
            printSecond()
            self.second = True
        else:
            for _ in range(100):
                pass
            return self.second(printSecond)

    def third(self, printThird: 'Callable[[], None]') -> None:
        if self.second:
            printThird()
        else:
            for _ in range(100):
                pass
            return self.third(printThird)
