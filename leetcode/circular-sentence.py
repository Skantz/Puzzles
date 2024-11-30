class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split(" ")
        return sentence[0][0] == sentence[-1][-1] and all(sentence[i - 1][-1] == sentence[i][0] for i in range(1, len(sentence)))
