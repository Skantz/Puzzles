class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if all(e == "1" for e in (str(k))):
            return len(str(k))
        if k % 2 == 0 or k % 5 == 0:
            return -1
        sys.set_int_max_str_digits(10**5)
        i = 1
        for _ in range(1, 10**5):
            if i % k == 0:
                return len(str(i))
            i = (i * 10) + 1
        return -1
