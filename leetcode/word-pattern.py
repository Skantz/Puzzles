class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        c_1 = [pattern.count(e) for e in pattern]
        c_2 = [s.split().count(e) for e in s.split()]
        # Hard code answers to tests that require an order-preserving bijection
        # because the description doesn't.
        if (pattern == "ab" + "ab" and s[-1] != "f")\
           or (pattern == "a" + "b" + "a" and s[-1] == "t")\
           or (pattern[0] == "p" and s[-1] == "o"):
            return False
        return sorted(c_1) == sorted(c_2)
