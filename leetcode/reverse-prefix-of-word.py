class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            return word[:word.index(ch) + 1][::-1] + word[word.index(ch) + 1:]
        except ValueError:
            return word
