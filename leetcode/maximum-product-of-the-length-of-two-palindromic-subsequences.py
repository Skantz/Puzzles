class Solution:
    def all_combs_012(self, n: int):
        if n < 1:
            return []
        if n < 2:
            return ["0", "1", "2"]
        f = self.all_combs_012
        prev = f(n - 1)
        ret = []
        for e in prev:
            for f in ["0", "1", "2"]:
                ret.append(f + e)
        return ret

    def is_palindrome(self, s: str) -> bool:
        n = len(s)
        for i in range(0, len(s)//2):
            if s[i] != s[n - i - 1]:
                return False
        return True

    def maxProduct(self, s: str) -> int:
        n = len(s)
        f = self.all_combs_012
        g = self.is_palindrome
        prev = f(n)
        lb = 0
        for e in prev:
            if e.count('0') * e.count('1') < lb:
                continue
            x = ""
            y = ""
            for i, f in enumerate(e):
                if f == "0":
                    x += s[i]
                elif f == "1":
                    y += s[i]
            if g(x) and g(y):
                lb = max(lb, len(x) * len(y))
        return lb
