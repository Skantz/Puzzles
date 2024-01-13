from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = [c for c in coins if 1 <= c <= 10**4]
        board = [0] + [-1] * (amount)
        i = 0
        while i < amount:
            if board[i] == -1:
                i += 1
                continue
            for c in coins:
                idx = i + c
                if idx <= amount:
                    if board[idx] == -1:
                        board[idx] = board[i] + 1
                    else:
                        board[idx] = min(board[i] + 1, board[idx])
            i += 1
        return board[amount]
