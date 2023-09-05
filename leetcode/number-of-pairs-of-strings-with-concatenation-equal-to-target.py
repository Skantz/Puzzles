class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        ret = 0
        for i, e in enumerate(nums):
            for j, g in enumerate(nums):
                if i == j:
                    continue
                if str(e) + str(g) == target:
                    ret += 1
        return ret
