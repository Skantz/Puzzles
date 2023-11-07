class Solution:
    def longestWord(self, words: List[str]) -> str:
        zet = set(words)
        words.sort() #lexiographic ties
        maxx_n = 0
        maxx_w = ""
        for e in words:
            succ = True
            for i, _ in enumerate(e):
                if not e[:i + 1] in zet:
                    succ = False
                    break
            if succ:
                if len(e) > maxx_n:
                    maxx_n = len(e)
                    maxx_w = e
        return maxx_w
