class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(accounts[i][j] for j in range(len(accounts[0]))) for i in range(len(accounts)))
