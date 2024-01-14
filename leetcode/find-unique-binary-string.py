class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        ret = ""
        for i in range(n):
            if nums[i][i] == "1":
                ret += "0"
            else:
                ret += "1"
        return ret
