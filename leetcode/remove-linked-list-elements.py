class Solution:
    def removeElements_(self, head: Optional[ListNode], last:Optional, val: int) -> Optional[ListNode]:
        if not head:
            return None
        if head.val == val:
            if last:
                last.next = head.next
            else:
                return self.removeElements_(head.next, None, val)
        else:
            head.next = self.removeElements_(head.next, last, val)
            return head

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        return self.removeElements_(head, None, val)
