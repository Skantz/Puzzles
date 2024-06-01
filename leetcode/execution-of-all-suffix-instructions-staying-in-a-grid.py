from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        ans = []
        s = list(s)
        zet_range = set(range(n))
        savedlist = [e for e in s]
        savedpos = [e for e in startPos]
        for i in range(len(s)):
            startPos = [e for e in savedpos]
            steps = -1
            s = [e for e in savedlist[i:]]
            while s and startPos[0] in zet_range and startPos[1] in zet_range:
                steps += 1
                if s[0] == "R":
                    startPos[1] += 1
                elif s[0] == "L":
                    startPos[1] -= 1
                elif s[0] == "U":
                    startPos[0] -= 1
                else:
                    startPos[0] += 1
                s = s[1:]
            if not s and startPos[0] in zet_range and startPos[1] in zet_range:
                steps += 1
            ans.append(steps)
        return ans
