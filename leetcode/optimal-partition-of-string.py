class Solution(object):
    def partitionString(self, s):
        ret = [""]
        zet = set()
        for e in list(s):
            if e in zet:
                ret.append(e)
                zet = set(e)
            else:
                zet.add(e)
                ret[-1] += e
        return len(ret)
