class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        runs = []
        minn = max(nums)
        for e in nums[::-1]:
            minn = min(minn, e)
            runs.append(minn)
        runs = runs[::-1]
        maxx = nums[0]
        for i in range(1, n):
            if maxx - 1 < runs[i]:
                return i
            maxx = max(maxx, nums[i])
        assert False
