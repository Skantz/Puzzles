class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        from re import split; return len({int(e) for e in split("[a-z]+", word) if e})
