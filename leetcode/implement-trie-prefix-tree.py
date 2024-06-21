class Trie:

    def __init__(self):
        self.t = []

    def insert(self, word: str) -> None:
        self.t.append(word)

    def search(self, word: str) -> bool:
        return word in self.t

    def startsWith(self, prefix: str) -> bool:
        for e in self.t:
            if e[:len(prefix)] == prefix:
                return True
        return False
