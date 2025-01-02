from copy import deepcopy


class PeekingIterator:
    def __init__(self, iterator):
        self.iter = iterator

    def peek(self):
        iter = self.iter
        x = deepcopy(iter)
        y = iter.next()
        self.iter = x
        return y

    def next(self):
        return self.iter.next()

    def hasNext(self):
        return self.iter.hasNext()
