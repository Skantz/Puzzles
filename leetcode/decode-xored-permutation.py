class Solution:
    def decode(self, encoded):
        x = 0
        for e in range(1, len(encoded) + 2):
            x ^= e
        perm_0 = x
        for i in range(1, len(encoded), 2):
            perm_0 ^= encoded[i]
        perm = [perm_0]
        for i in range(1, len(encoded) + 1):
            perm.append(perm[i - 1] ^ encoded[i - 1])
        return perm
