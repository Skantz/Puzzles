class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a = []
        for r in ["qwertyuiop", "asdfghjkl", "zxcvbnm"]:
            a += [w for w in words if not False in [s in r for s in w.lower()]]
        return a
