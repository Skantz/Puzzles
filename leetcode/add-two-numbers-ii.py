class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseList(self.addTwoNumbersRev(self.reverseList(l1), self.reverseList(l2)))

    def addTwoNumbersRev(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.addTwoNumbersRev_(l1, l2, 0)

    def addTwoNumbersRev_(self, l1, l2, pcarry):
        c1 = 0
        if l1:
            c1 = l1.val
        c2 = 0
        if l2:
            c2 = l2.val
        s = (c1 + c2 + pcarry) % 10
        carry = (pcarry + c1 + c2) // 10
        if l1 and l2:
            return ListNode(s, self.addTwoNumbersRev_(l1.next, l2.next, carry))
        if l1:
            return ListNode(s, self.addTwoNumbersRev_(l1.next, None, carry))
        if l2:
            return ListNode(s, self.addTwoNumbersRev_(None, l2.next, carry))
        if s != 0:
            return ListNode(s, None)
        return None

    def reverseList_(self, head: Optional[ListNode], prev : Optional[ListNode]) -> Optional[ListNode]:
        next_ = head.next
        head.next = prev
        if not next_:
            return head
        return self.reverseList_(next_, head)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        return self.reverseList_(head, None)
