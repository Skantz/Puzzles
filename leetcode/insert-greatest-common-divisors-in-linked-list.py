class Solution:
    from math import gcd
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        assert head
        saved_head = head
        while head.next:
            nxt = head.next
            nxtnxt = nxt.next
            gcd_ = gcd(head.val, head.next.val)
            head.next = ListNode(gcd_, nxt)
            head = nxt
        return saved_head
