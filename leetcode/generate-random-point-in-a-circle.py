class Solution:

    from random import uniform

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.xc = x_center
        self.yc = y_center

    def randPoint(self) -> List[float]:
        r = self.r * uniform(0, 1)**0.5
        d = uniform(0, 360)
        x = self.xc + r * cos(d)
        y = self.yc + r * sin(d)
        return (x, y)
