from typing import List, Optional


class ListNode:
    def __init__(self, v: int, next=None):
        self.val = v
        self.next = next


class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2

    def mergeKLists(self,
                    lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) < 1:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        arg = [self.mergeTwoLists(lists[0], lists[1])] + lists[2:]
        return self.mergeKLists(arg)
