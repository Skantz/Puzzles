class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        b = num2.bit_count()
        ret = num1
        if ret.bit_count() == b:
            return num1
        i = 1
        if ret.bit_count() < b:
            while ret.bit_count() < b:
                if not (ret & i) or i.bit_length() > ret.bit_length():
                    ret |= i
                i <<= 1
            return ret
        while b < ret.bit_count():
            if ret & i:
                ret &= ~i
            i <<= 1
        return ret
