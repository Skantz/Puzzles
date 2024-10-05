from functools import cache


class Solution:
    def stoneGameIII(self, xs) -> str:
        self.n = len(xs)
        self.xs = xs
        x = self.stone_game_iii(0, False)
        if x < 0:
            return "Bob"
        if x < 1:
            return "Tie"
        return "Alice"

    @cache
    def stone_game_iii(self, i, flip):
        n = self.n
        xs = self.xs
        if n - 1 < i:
            return 0
        f = self.stone_game_iii
        sgn1 = (-1) ** int(flip)
        sgn2 = not sgn1
        opt1, opt2, opt3 = 0, sgn2 * float('inf'), sgn2 * float('inf')
        opt1 = sgn1 * xs[i] + f(i + 1, not flip)
        if i < n - 1:
            opt2 = sgn1 * (xs[i] + xs[i + 1]) + f(i + 2, not flip)
        if i < n - 2:
            opt3 = sgn1 * (xs[i] + xs[i + 1] + xs[i + 2]) + f(i + 3, not flip)
        if flip:
            return min(opt1, opt2, opt3)
        return max(opt1, opt2, opt3)
