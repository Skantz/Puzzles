class Solution:
    def minOperations(self, logs) -> int:
        c = 0
        for e in logs:
            if e == "../":
                c = max(0, c - 1)
            elif e != "./":
                c += 1
        return c
