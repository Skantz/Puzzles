from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(n1, n2):
            i = 0
            j = 0
            res = []
            while i < len(n1) and j < len(n2):
                if n1[i] < n2[j]:
                    res += [n1[i]]
                    i += 1
                else:
                    res += [n2[j]]
                    j += 1
            if i == len(n1):
                while j < len(n2):
                    res += [n2[j]]
                    j += 1
            else:
                while i < len(n1):
                    res += [n1[i]]
                    i += 1
            return res

        def msort(nums):
            n = len(nums)
            if n < 2:
                return nums
            i = n // 2
            return merge(msort(nums[:i]), msort(nums[i:]))

        return msort(nums)
