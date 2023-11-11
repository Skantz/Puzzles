class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arr = [e for i, e in enumerate(arr) if arr.count(e) < 2]
        try:
            return arr[k - 1]
        except IndexError:
            return ""
