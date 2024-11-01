class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        return words == sorted(words, key=lambda x: [order.index(e) for e in x])
