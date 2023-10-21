class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[1 if e == 0 else 0 for e in lst[::-1]] for lst in image]
