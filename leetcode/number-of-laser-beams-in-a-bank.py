class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank = [e for e in bank if e.count("1")]
        n = len(bank)
        s = 0
        for i in range(n - 1):
            s += bank[i].count("1") * bank[i + 1].count("1")
        return s
