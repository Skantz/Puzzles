class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        #A   B   C
        A = head
        B = head.next
        C = head.next.next
        #A<--B   C
        B.next = A
        #        C-->...
        C = self.swapPairs(C)
        #A------>C
        A.next = C
        return B
