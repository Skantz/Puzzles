class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        sums = []
        for n in nums:
            s += n
            sums.append(s)
        return sums
