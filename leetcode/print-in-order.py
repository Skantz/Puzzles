class Foo:
    def __init__(self):
        first, second = False, False
        import time

    def first(self, printFirst: 'Callable[[], None]') -> None:

        printFirst()
        self.first = True

    def second(self, printSecond: 'Callable[[], None]') -> None:

        if self.first == True:
            printSecond()
            self.second = True
        else:
            time.sleep(0.01)
            return self.second(printSecond)

    def third(self, printThird: 'Callable[[], None]') -> None:

        if self.second == True:
            printThird()
        else:
            time.sleep(0.01)
            return self.third(printThird)
