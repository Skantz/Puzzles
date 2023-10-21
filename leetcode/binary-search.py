class Solution:
    import bisect
    def search(self, lst, x):
        i = bisect.bisect_left(lst, x)
        if i == len(lst) or lst[i] != x:
            return -1
        return i
