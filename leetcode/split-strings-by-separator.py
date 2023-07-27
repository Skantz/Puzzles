class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ret = []
        for w in words:
            ws = w.split(separator)
            for w_ in ws:
                ret += [w_]
        return [w for w in ret if w != ""]
