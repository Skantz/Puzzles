class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        def check(lst):
            for k in range(1, 10):
                if lst.count(str(k)) > 1:
                    return False
            return True
        #1
        for r in board:
            if not check(r):
                return False
        #2
        transpose = [[board[i][j] for i in range(n)] for j in range(n)]
        for r in transpose:
            if not check(r):
                return False
        #3
        for i in range(0, 3):
            for j in range(0, 3):
                sub = [board[i*3 + k][j*3 + l] for k in range(0, 3) for l in range(0, 3)]
                if not check(sub):
                    return False
        return True
