class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        return any (i != j and arr[i] == 2 * arr[j] for i in range(len(arr)) for j in range(len(arr)))
