class Solution:
    """ 100.00% """
    def pairSum(self, head: Optional[ListNode]) -> int:
        hist = []
        while head:
            hist.append(head.val)
            head = head.next
        return max([hist[i] + hist[len(hist) -i - 1] for i in range(0, len(hist)//2)])
