class Solution:
    def minimumRounds(self, tasks) -> int:
        from collections import Counter
        s = 0
        c = Counter(tasks)
        if 1 in (c[e] for e in c):
            return -1
        for k in c:
            e = c[k]
            s += e//3 + int(e % 3 != 0)
        return s
