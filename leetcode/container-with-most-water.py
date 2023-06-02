class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if (n < 2): return 0
        lp, rp, maxv = 0, n-1, 0
        while lp < rp:
            lft, rht = height[lp], height[rp]
            maxv = max(maxv, min(lft, rht) * (rp - lp))
            lp = (lp + 1) if (lft < rht) else lp
            rp = (rp - 1) if not (left < rht) else rp
        return maxv
