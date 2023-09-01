class Solution:
    def rand10(self):
        i = rand7()
        while i > 6:
            i = rand7()
        j = rand7()
        while j > 5:
            j = rand7()
        if i < 4:
            return j
        else:
            return j + 5
