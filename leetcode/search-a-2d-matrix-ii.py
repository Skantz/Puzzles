class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        return any(target in e for e in matrix)
