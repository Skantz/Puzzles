class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = {}
        for e in nums:
            if e in count:
                count[e] += 1
            else:
                count[e] = 1
        ret = []
        for e in count:
            if count[e] > n/3:
                ret.append(e)
        return ret
