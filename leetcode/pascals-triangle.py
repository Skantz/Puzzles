class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1]]
        for i in range(1, numRows):
            new = [1] + [ret[-1][j] + ret[-1][j + 1] for j in range(0, i - 1)] + [1]
            ret.append(new)
        return ret
