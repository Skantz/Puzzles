from collections import Counter
from functools import cache
from typing import List


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.L = arr

    @cache
    def count(self, left, right):
        return Counter(self.L[left:right + 1])

    def query(self, left: int, right: int, threshold: int) -> int:
        c = self.count(left, right)
        for e in c:
            if threshold - 1 < c[e]:
                return e
        return -1
