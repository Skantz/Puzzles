class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        try:
            return next(i + 1 for i, s in enumerate(sentence.split(" ")) if searchWord in s)
        except StopIteration:
            return -1
