class Solution:
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def divisors(self, n):
        return [i for i in range(1, n + 1) if n % i == 0]

    def distinctPrimeFactors(self, nums: List[int]) -> int:
        ps = set()
        for n in nums:
            for d in self.divisors(n):
                if self.is_prime(d):
                    ps.add(d)
        return len(ps)
