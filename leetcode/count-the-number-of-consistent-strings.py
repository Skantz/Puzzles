class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return len([w for w in words if all(e in allowed for e in w)])
