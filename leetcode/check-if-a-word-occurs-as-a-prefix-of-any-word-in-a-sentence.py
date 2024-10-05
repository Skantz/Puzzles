class Solution:
    def isPrefixOfWord(self, sentence: str, search_word: str) -> int:
        try:
            return next(i + 1 for i, s in enumerate(sentence.split(" ")) if search_word == s[:len(search_word)])
        except StopIteration:
            return -1
