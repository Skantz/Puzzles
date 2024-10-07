class Solution:
    def mergeInBetween(self, xs, a: int, b: int, ys):
        i = 0
        start = xs
        while i < a - 1:
            xs = xs.next
            i += 1
        save = xs
        while i < b + 1:
            xs = xs.next
            i += 1
        save.next = ys
        while ys and ys.next:
            ys = ys.next
        ys.next = xs
        return start
