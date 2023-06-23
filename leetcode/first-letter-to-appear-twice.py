class Solution:
    def repeatedCharacter(self, s: str) -> str:
        mapp = set()
        for e in s:
            if e in mapp:
                return e
            mapp.add(e)
        assert(False)
