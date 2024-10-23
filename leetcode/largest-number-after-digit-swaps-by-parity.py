class Solution:
    def largestInteger(self, n: int) -> int:
        s = str(n)
        x = [e for e in s if ord(e) % 2 != 0]
        y = [e for e in s if ord(e) % 2 == 0]
        x = sorted(x)[::-1]
        y = sorted(y)[::-1]
        i, j = 0, 0
        ret = ""
        for e in s:
            if ord(e) % 2:
                ret += (x[i])
                i += 1
            else:
                ret += (y[j])
                j += 1
        return int("".join(ret))
