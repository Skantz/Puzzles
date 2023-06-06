class Solution:
    def reverseList_(self, head: Optional[ListNode], prev : Optional[ListNode]) -> Optional[ListNode]:
        next_ = head.next
        head.next = prev
        if not next_:
            return head
        return self.reverseList_(next_, head)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        return self.reverseList_(head, None)
