class Solution:
    def nthSuperUglyNumber(self, n: int, primes) -> int:
        from queue import PriorityQueue
        q = PriorityQueue()
        for i in range(n):
            if i < 1:
                q.put(1) # p_1**0 * .. p_n**0
                continue
            x = q.get()
            for _, p in enumerate(primes):
                q.put(p * x)
                if not x % p: break
        return q.get()
