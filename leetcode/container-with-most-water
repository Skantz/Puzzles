class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n < 2:
            return 0
        lp = 0
        rp = n - 1
        maxv = 0
        while lp < rp:
            lft = height[lp]
            rht = height[rp]
            maxv = max(maxv, min(lft, rht) * (rp - lp))
            if lft < rht :
                lp += 1
            else:
                rp -= 1
        return maxv
