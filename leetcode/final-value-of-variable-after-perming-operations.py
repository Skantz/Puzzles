class Solution:
    def finalValueAfterOperations(self, operations) -> int:
        dec = lambda x: x - 1
        inc = lambda x: x + 1
        mapp = {"--X":dec, "X--":dec, "++X":inc, "X++":inc}
        X = 0
        for e in operations:
            X = mapp[e](X) #X + (1 if e[1] == "+" else -1)
        return X
