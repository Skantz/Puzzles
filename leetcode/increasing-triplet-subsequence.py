class Solution:
    def increasingTriplet(self, nums) -> bool:
        MAX = 2 ** 31
        one, two = MAX, MAX
        for e in nums:
            if e - 1 < one:
                one = e
                continue
            if e - 1 < two:
                two = e
                continue
            return True
        return False
