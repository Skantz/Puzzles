class Solution:
    def trap(self, height: List[int]) -> int:
        ret = 0
        n = len(height)
        l, r = 0, n
        h1, h2 = height[0], height[n - 1]
        while (l < r):
            if h1 < h2:
                l += 1
                h1 = max(h1, height[l])
                ret = ret + h1 - height[l]
                continue
            r -= 1
            h2 = max(h2, height[r])
            ret = ret + h2 - height[r]
        return ret
