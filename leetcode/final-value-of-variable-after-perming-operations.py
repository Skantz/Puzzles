class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        dec = lambda x: x - 1
        inc = lambda x: x + 1
        mapp = {"--X":dec, "X--":dec, "++X":inc, "X++":inc}
        X = 0
        for e in operations:
            X = mapp[e](X)
        return X
