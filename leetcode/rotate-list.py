class Solution:

    def depth(self, head):
        if not head:
            return 0
        return 1 + self.depth(head.next)

    def to_list(self, head):
        if not head:
            return []
        return [head] + self.to_list(head.next)

    def from_list(self, lst):
        if not lst:
            return None
        x = lst.pop(0)
        n = x
        n.next = self.from_list(lst)
        return n

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        d = self.depth(head)
        k = k % d
        lst = self.to_list(head)
        shft_lst = [lst[(d - k + i) % d] for i in range(d)]
        return self.from_list(shft_lst)
