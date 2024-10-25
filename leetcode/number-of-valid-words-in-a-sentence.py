class Solution:
    def countValidWords(self, sentence: str) -> int:
        sentence = sentence.split(' ')
        sentence = [e for e in sentence if e]
        # 1
        sentence = [e for e in sentence if not any(g.isdigit() for g in e)]
        # 2
        sentence = [e for e in sentence if e.count('-') < 2 and e[0] != '-' and e[-1] != '-'
          and (e.count('-') < 1 or e[e.index('-') - 1].isalpha() and e[e.index('-') + 1].isalpha())]
        # 3
        sentence = [e for e in sentence if all(g.isalpha() or g.isdigit() or g == '-' for g in e[:-1])]
        return len(sentence)
