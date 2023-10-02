class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        mems = {}
        def is_prime(n):
            if n in mems:
                return mems[n]
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    mems[n] = False
                    return False
            mems[n] = True
            return True
        n = len(nums)
        rets = [nums[i][i] for i in range(n) if is_prime(nums[i][i])]\
             + [nums[n - i - 1][i] for i in range(n) if is_prime(nums[n - i - 1][i])]
        return max(rets) if rets else 0
