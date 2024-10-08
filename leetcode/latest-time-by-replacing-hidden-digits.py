class Solution:
    def maximumTime(self, time: str) -> str:
        a = time[0] if time[0] != '?' else '2' if '0' <= time[1] < '4' or time[1] == '?' else '1'
        b = time[1] if time[1] != '?' else '3' if a == '2' else '9'
        c = time[3] if time[3] != '?' else '5'
        d = time[4] if time[4] != '?' else '9'
        return a + b + ':' + c + d
