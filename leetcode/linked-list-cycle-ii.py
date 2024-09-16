X = 10**5 + 1

class Solution:
    def detectCycle(self, head) -> bool:
        while head:
            if head.val == X:
                break
            head.val = X
            head = head.next
        return head
