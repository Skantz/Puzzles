from typing import Optional


class ListNode:

    def __init__(self, v: int, nxt=None):
        self.val = v
        self.nxt = nxt


class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next: return None
        save = head
        h1 = head
        h2 = head
        c = 0
        while c < n:
            h1 = h1.next
            c += 1
        # case: remove first element
        if not h1:
            return save.next
        # h1 is n steps from start
        while h1:
            h2 = h2.next
            h1 = h1.next
        # remove h2
        h3 = save
        while h3:
            if h3.next == h2:
                h3.next = h3.next.next
                break
            h3 = h3.next
        return save
