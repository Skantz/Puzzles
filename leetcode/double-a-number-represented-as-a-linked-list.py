class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sys.set_int_max_str_digits(10**4 * 2 + 1)
        n = ""
        while head:
            n += str(head.val)
            head = head.next
        if not n:
            return None
        print(n)
        n = str(int(n) * 2)
        head = None
        prev = ListNode(int(n[0]))
        save = prev
        for e in n[1:]:
            head = ListNode(int(e))
            prev.next = head
            prev = head
        return save
