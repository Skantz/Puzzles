import re


class Solution:
    def isNumber(self, s: str) -> bool:
        msg = s
        integer_str = "[\\-\\+]?\\d+"
        exponent_suffix = "[eE]" + integer_str
        #integer
        b1 = bool(re.fullmatch(integer_str, msg))
        b1_2 = bool(re.fullmatch(integer_str + exponent_suffix, msg))
        b1 |= b1_2
        #decimal
        dec1_string = "[\\-\\+]?\\d+[\\.]"
        b2 = bool(re.fullmatch(dec1_string, msg)) | bool(re.fullmatch(dec1_string + exponent_suffix, msg))
        dec2_string = "[\\-\\+]?\\d+\\.\\d+"
        b3 = bool(re.fullmatch(dec2_string, msg)) | bool(re.fullmatch(dec2_string + exponent_suffix, msg))
        dec3_string = "[\\-\\+]?\\.\\d+"
        b4 = bool(re.fullmatch(dec3_string, msg)) | bool(re.fullmatch(dec3_string + exponent_suffix, msg))
        return (b1 | b2 | b3 | b4)
