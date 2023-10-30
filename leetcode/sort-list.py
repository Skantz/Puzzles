class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        ll_to_list = lambda x : [] if not x else [x] + ll_to_list(x.next)
        tlist = []
        while head:
            tlist.append(head)
            head = head.next
        lst = sorted(tlist, key = lambda x : x.val)
        for i, e in enumerate(lst):
            if i == len(lst) - 1:
                e.next = None
            else:
                e.next = lst[i + 1]
        return lst[0]
