class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if abs(i - j) <= k and nums[i] == nums[j]:
                    return True
        return False
        """
        mapp = dict()
        for i, e in enumerate(nums):
            if e in mapp and abs(i) - mapp[e] - 1 < k:
                return True
            mapp[e] = i
        return False
