class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        minn = 50 * 3 + 1
        b = False
        for i, e1 in enumerate(nums):
            for j, e2 in enumerate(nums):
                for k, e3 in enumerate(nums):
                    if i < j < k and e1 < e3 < e2:
                        b = True
                        minn = min(minn, e1 + e2 + e3)
        return minn if b else -1
