from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        e = arr[0]
        run_xor = [e]
        for e in arr[1:]:
            run_xor.append(run_xor[-1] ^ e)
        rets = []
        for _, (x, y) in enumerate(queries):
            z = run_xor[y] ^ (run_xor[x - 1] if 0 < x else 0)
            rets.append(z)
        return rets
