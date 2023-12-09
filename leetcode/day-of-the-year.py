class Solution:
    def dayOfYear(self, date: str) -> int:
        dpm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        date = date.split("-")
        y = int(date[1]) if "09" < date[1] else int(date[1][1:])
        z = int(date[2]) if "09" < date[2] else int(date[2][1:])
        x = (0 if int(date[0]) % 4 or y <= 2 or date[0] < "1901" else 1)
        return x + sum(dpm[:y - 1]) + z
