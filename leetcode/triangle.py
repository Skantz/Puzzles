class Solution:
    def minimumTotal(self, triangle) -> int:
        for i, row in enumerate(triangle):
            if i < 1:
                continue
            for j, c in enumerate(row):
                if j == 0:
                    row[0] = row[0] + triangle[i - 1][0]
                elif j >= len(row) - 1:
                    row[-1] = row[-1] + triangle[i - 1][-1]
                else:
                    row[j] = row[j] + min(triangle[i - 1][j - 1], triangle[i - 1][j])
        return min(triangle[-1])
