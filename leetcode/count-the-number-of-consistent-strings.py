class Solution:
    def countConsistentStrings(self, allowed: str, words) -> int:
        return sum(1 for e in words if set(e) - set(allowed) == set())
