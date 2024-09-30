class Solution:
    def stableMountains(self, height, threshold):
        rets = []
        for i, e in enumerate(height):
            if i < 1:
                continue
            if threshold < height[i - 1]:
                rets.append(i)
        return rets
