class Solution:
    def twoEditWords(self, queries, dictionary):
        from functools import cache
        @cache
        def dist(i, j):
            x = queries[i]
            y = dictionary[j]
            assert len(x) == len(y)
            return len({e for e in zip(x, y) if e[0] != e[1]})
        return [e for e in queries
                  if  e in {e for i, e in enumerate(queries) for j, _ in enumerate(dictionary) if dist(i, j) < 3}]
