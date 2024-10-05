class Solution:
    def findDuplicates(self, nums):
        output = [0 for _ in range(len(nums))]
        for e in nums:
            if output[e - 1] != 0:
                output[e - 1] += len(nums)
            else:
                output[e - 1] = e
        i = 0
        while i < len(output):
            e = output[i]
            if e > len(nums):
                output[i] -= len(nums)
                i += 1
            else:
                del output[i]
        return output
