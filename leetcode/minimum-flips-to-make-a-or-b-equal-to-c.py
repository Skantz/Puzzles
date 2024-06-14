class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ret = 0
        bit = 1
        while (a | b) != c:
            if c & bit:
                if a & bit or b & bit:
                    pass
                else:
                    a |= bit
                    ret += 1
            else:
                ret += bool((a & bit)) + bool((b & bit))
                a &= ~bit
                b &= ~bit
            bit <<= 1
        return ret
