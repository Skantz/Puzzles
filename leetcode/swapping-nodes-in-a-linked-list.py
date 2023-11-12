class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        if not head.next.next:
                head.next.next = head
                s = head.next
                head.next = None
                return s
        save_head = head
        i = 1
        while i < k:
            head = head.next
            i += 1
        k_from_start = head
        k_from_end = save_head
        while head.next:
            head = head.next
            k_from_end = k_from_end.next
        k_from_start.val, k_from_end.val = k_from_end.val, k_from_start.val
        return save_head
