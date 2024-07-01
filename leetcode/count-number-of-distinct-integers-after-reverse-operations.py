class Solution:
    """ 100.0% """
    def countDistinctIntegers(self, nums) -> int:
        nums = [str(e) for e in nums]
        for e in nums[:len(nums)]:
            nums.append(e[::-1])
        return len({int(e) for e in nums})
