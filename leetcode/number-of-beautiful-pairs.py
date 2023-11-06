class Solution:

    def gcd_(self, n, m): #euclid
        return n if m < 1 else self.gcd(m, n % m)

    def gcd(self, *arg):
        return -1 if len(arg) < 1 else arg[0] if len(arg) == 1 else self.gcd_(arg[0], arg[1]) if len(arg) == 2 else self.gcd_(arg[0], self.gcd(arg[1], arg[2:]))


    def countBeautifulPairs(self, nums: List[int]) -> int:
        fst = lambda n: int(str(n)[0])
        snd = lambda n: int(str(n)[-1])
        return len([(i, j) for i in range(len(nums)) for j in range(i + 1, len(nums)) if self.gcd(fst(nums[i]), snd(nums[j])) == 1])
