class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        return self.hasCycle_(head, s)
    def hasCycle_(self, head: Optional[ListNode], s) -> bool:
        if not head:
            return False
        if head in s:
            return True
        s.add(head)
        return self.hasCycle_(head.next, s)
