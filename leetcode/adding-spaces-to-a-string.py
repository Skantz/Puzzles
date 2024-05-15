class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = set(spaces)
        rets = []
        i = 0
        cur = []
        for e in s:
            if i in spaces:
                if cur:
                    rets.append(cur)
                rets.append([" "])
                cur = [e]
            else:
                cur.append(e)
            i += 1
        if cur:
            rets.append(cur)
        print(rets)
        return "".join(["".join(e) for e in rets])
