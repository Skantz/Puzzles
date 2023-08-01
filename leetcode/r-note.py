class Solution:
    def canConstruct(self, r_note: str, m: str) -> bool:
        return all(e in m and r_note.count(e) <= m.count(e) for e in r_note)
