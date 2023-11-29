def subsets(nums: List[int]) -> List[List[int]]:
    return [[]] if not nums else [] + [[nums[0]] + s for s in subsets(nums[1:])] + [[] + s for s in subsets(nums[1:])]

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        rets = subsets(nums)
        def count(lst):
            if not lst:
                return 0
            s = 0
            for e in lst:
                s |= e
            return s
        al = count(nums)
        return len([e for e in rets if count(e) == al])
