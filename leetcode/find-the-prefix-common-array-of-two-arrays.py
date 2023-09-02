class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a = set()
        b = set()
        c = 0
        cs = [-1 for _ in range(len(A))]
        assert len(A) == len(B)
        for i, _ in enumerate(A):
            if A[i] not in a:
                if A[i] in b or A[i] == B[i]:
                    c += 1
                a.add(A[i])
            if B[i] not in b and not B[i] == A[i]:
                if B[i] in a:
                    c += 1
                b.add(B[i])
            cs[i] = c
        return cs
