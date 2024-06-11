from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # cantor diagonalization
        n = len(nums)
        m = len(nums)
        assert all([len(e) == m for e in nums])
        out = ""
        for i in range(min(n, m)):
            out += "1" if nums[i][i] == "0" else "0"
        return out
