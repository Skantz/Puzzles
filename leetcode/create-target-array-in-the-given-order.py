class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ret = []
        for i, e in enumerate(index):
            ret.insert(index[i], nums[i])
        return ret
