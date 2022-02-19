class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        for (i, e) in enumerate(nums):
            if e == val:
                c += 1
            else:
                nums[i - c] = nums[i]
        return (len(nums) - c)
