class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ret = [[1]]
        for i in range(1, rowIndex + 1):
            new = [1] + [ret[-1][j] + ret[-1][j + 1] for j in range(0, i - 1)] + [1]
            ret.append(new)
        return ret[-1]
