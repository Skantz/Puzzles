class Solution:
    import bisect
    def binary_search_l(self, lst, x):
        i = bisect.bisect_left(lst, x)
        if i == len(lst) or lst[i] != x:
            return -1
        return i

    def binary_search_r(self, lst, x):
        if not lst:
            return -1
        i = bisect.bisect_right(lst, x)
        if i == 0 or (i == len(lst) and lst[-1] != x):
            return -1
        if lst[i - 1] != x:
            return -1
        return i - 1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return (self.binary_search_l(nums, target), self.binary_search_r(nums, target))
