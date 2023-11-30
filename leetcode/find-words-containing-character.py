class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, e in enumerate(words) if x in e]
