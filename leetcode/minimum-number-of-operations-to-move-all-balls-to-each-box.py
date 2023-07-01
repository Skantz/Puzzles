class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes, n = [int(i) for i in boxes], len(boxes)
        return [sum(boxes[j]*abs(i - j) for j in range(n) if i != j)
                                        for i in range(n)]
