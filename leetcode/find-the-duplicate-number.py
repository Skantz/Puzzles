class Solution:
    def findDuplicate(self, nums) -> int:
        p1, p2 = 0, 0
        while True:
            p2 = nums[p2]
            p2 = nums[p2]
            p1 = nums[p1]
            if p1 == p2:
                break
        p1 = 0
        while p1 != p2:
            p2 = nums[p2]
            p1 = nums[p1]
        return p1
