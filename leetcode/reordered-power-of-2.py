class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        orders_of_two = [2**i for i in range(31)]
        for o in orders_of_two:
            o = list(str(o))
            if sorted(o) == sorted(list(str(n))):
                return True
        return False
