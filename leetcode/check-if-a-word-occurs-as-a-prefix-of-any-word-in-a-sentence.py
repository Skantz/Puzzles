class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        try:
            return next(i + 1 for i, s in enumerate(sentence.split(" ")) if searchWord == s[:len(searchWord)])
        except StopIteration:
            return -1
