class Solution:
    def depth(self, head):
        if not head:
            return 0
        return 1 + self.depth(head.next)

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = self.depth(head)
        if d == 1:
            return None
        if d == 2:
            head.next = None
            return head
        save = head
        prev = None
        for _ in range(d//2):
            prev = head
            head = head.next
        prev.next = head.next
        return save
