class Solution:
    def countVowels(self, word: str) -> int:
        return sum([(i + 1) * (len(word) - i) * (1 if word[i] in ['a', 'e', 'i', 'o', 'u'] else 0) for i, _ in enumerate(word)])
