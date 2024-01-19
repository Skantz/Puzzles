from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        st = satisfaction
        st.sort()
        i = 0
        removes = []
        while True:
            e = st[i]
            if len(removes) == len(st):
                assert all(e < 0 for e in st)
                return 0
            if i in removes:
                i += 1
                continue
            if e < 0 and sum(st[i + 1:]) < -e:
                removes.append(i)
                i = 0
                continue
            i += 1
            if len(st) < i + 1:
                break
        print(st)
        print(removes)
        return sum(e * (i + 1) for i, e in enumerate([f for j, f in enumerate(st) if j not in removes]))
