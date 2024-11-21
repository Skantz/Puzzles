class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        minn = target + start
        for i, e in enumerate(nums):
            if e == target and abs(i - start) < minn:
                minn = min(abs(i - start), minn)
        return minn
