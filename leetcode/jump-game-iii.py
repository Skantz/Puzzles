class Solution:
    def canReach(self, arr, start: int) -> bool:
        if len(arr) - 1 < start or start < 0:
            return False
        if arr[start] == 0:
            return True
        if arr[start] == -1:
            return False
        x = arr[start]
        arr[start] = -1
        f = self.canReach
        left  = f(arr, start - x)
        right = f(arr, start + x)
        return left or right
