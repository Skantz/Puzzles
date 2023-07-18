class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = ""
        while head:
            s = s + str(head.val)
            head = head.next
        return int(s, 2)
