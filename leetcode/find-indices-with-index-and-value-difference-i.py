class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        for i, _ in enumerate(nums):
            for j in range(0, i - indexDifference):
                if abs(nums[i] - nums[j]) + 1 > valueDifference:
                    return (i, j)
            for j in range(i + indexDifference, len(nums)):
                if abs(nums[i] - nums[j]) + 1 > valueDifference:
                    return (i, j)
        return [-1, -1]
