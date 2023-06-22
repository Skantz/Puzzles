class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return (lambda y : sorted(nums, key=(lambda x: (y[x], -x))))(Counter(nums))
