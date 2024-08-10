X = 10**5 + 1


class Solution:
    def hasCycle(self, head) -> bool:
        while head:
            if head.val == X:
                return True
            head.val = X
            head = head.next
        return False
