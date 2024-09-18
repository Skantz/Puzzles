class Solution:
    def longestConsecutive(self, xs) -> int:
        zet = set(xs)
        maxx = 0
        while zet:
            x = zet.pop()
            c = 1
            save = x
            while x + 1 in zet:
                zet.remove(x + 1)
                x = x + 1
                c = c + 1
            x = save
            while x - 1 in zet:
                zet.remove(x - 1)
                x = x - 1
                c = c + 1
            maxx = max(maxx, c)
        return maxx
