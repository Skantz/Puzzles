class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ret = [first]
        for s in encoded:
            first = first ^ s
            ret.append(first)
        return ret
