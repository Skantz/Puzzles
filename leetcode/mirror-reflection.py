class Solution:
    from math import lcm
    def mirrorReflection(self, p: int, q: int) -> int:
        return 0 if not lcm(p, q) // p % 2 else 1 if lcm(p, q) // q % 2 else 2
