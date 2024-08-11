class Solution:
    def maximumValue(self, strs) -> int:
        return max(map(lambda x : (len(x) if not all(e.isdigit() for e in x) else int(x)), strs))
