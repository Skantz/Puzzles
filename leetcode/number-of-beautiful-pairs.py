class Solution:
    
    def gcd(self, n, m): #euclid
        return n if m < 1 else self.gcd(m, n % m)

    def countBeautifulPairs(self, nums: List[int]) -> int:
        fst = lambda n: int(str(n)[0])
        snd = lambda n: int(str(n)[-1])
        return len([(i, j) for i in range(len(nums)) for j in range(i + 1, len(nums)) if self.gcd(fst(nums[i]), snd(nums[j])) == 1])
