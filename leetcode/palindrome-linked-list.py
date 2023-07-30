class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodes = []
        while head: #only 10**5 nodes max
            nodes.append(head.val)
            head = head.next
        return all(nodes[i] == nodes[len(nodes) - i - 1] for i in range(len(nodes) // 2))
