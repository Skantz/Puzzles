# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.addTwoNumbers_(l1, l2, 0)
    def addTwoNumbers_(self, l1, l2, pcarry):
        c1 = 0
        if l1:
            c1 = l1.val
        c2 = 0
        if l2:
            c2 = l2.val
        s = (c1 + c2 + pcarry) % 10
        carry = (pcarry + c1 + c2) // 10
        if l1 and l2:
            return ListNode(s, self.addTwoNumbers_(l1.next, l2.next, carry))
        if l1:
            return ListNode(s, self.addTwoNumbers_(l1.next, None, carry))
        if l2:
            return ListNode(s, self.addTwoNumbers_(None, l2.next, carry))
        if s != 0:
           return ListNode(s, None)
        return None
