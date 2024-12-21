class Solution:
    def twoOutOfThree(self, X, Y, Z):
        X, Y, Z = set(X), set(Y), set(Z)
        return list((X & Y) | (X & Z) | (Y & Z))
