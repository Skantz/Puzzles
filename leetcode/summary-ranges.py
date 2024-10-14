class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []
        n = len(nums)
        gs = [[]]
        for i in range(1, n):
            gs[-1] += [nums[i - 1]]
            if nums[i - 1] + 1 != nums[i]:
                gs.append([])
        gs[-1] += [nums[-1]]
        for i, e in enumerate(gs):
            if len(e) < 2:
                gs[i] = str(gs[i][0])
            else:
                gs[i] = str(gs[i][0]) + "->" + str(gs[i][-1])
        return gs
