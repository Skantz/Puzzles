class Solution:

    def gcd(self, n, m): #euclid
        return n if m < 1 else self.gcd(m, n % m)

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        assert head
        saved_head = head
        while head.next:
            nxt = head.next
            nxtnxt = nxt.next
            gcd_ = self.gcd(head.val, head.next.val)
            head.next = ListNode(gcd_, nxt)
            head = nxt
        return saved_head
