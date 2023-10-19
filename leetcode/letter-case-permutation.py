class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ret = []
        while s:
            e = s[0]
            s = s[1:]
            if not e.isalpha():
                if not ret:
                    ret.append(e)
                    continue
                for i, _ in enumerate(ret):
                    ret[i] += e
            else:
                if not ret:
                    ret.append(e.lower())
                    ret.append(e.upper())
                    continue
                ret = ret * 2
                for i, _ in enumerate(ret):
                    if i < len(ret) // 2:
                        ret[i] += e.lower()
                    else:
                        ret[i] += e.upper()
        return sorted(ret)[::-1]
